# Electrocredible.com, Language: MicroPython
import time
import machine
import network
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import urequests as requests
import utime

ssid = 'Asus ROG Phone'
password = 'sakib dalal'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

WIDTH  = 128                                          
HEIGHT = 64


button1 = Pin(3, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Wait for connection to establish
max_wait = 10

while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
            break
    max_wait -= 1
    print('waiting for connection...')
    oled.fill(0)
    oled.text("Waiting for",0,0)
    oled.text("Connection...",0,8)
    oled.text("X  O    ", 48, 25)
    oled.text(" __  ", 48, 45)
    oled.show()
    oled.fill(0)
    utime.sleep(0.2)
    oled.text("Waiting for",0,0)
    oled.text("Connection...",0,8)
    oled.text("O  X    ", 48, 25)
    oled.text(" __  ", 48, 45)
    oled.show()
    time.sleep(1)
    
# Manage connection errors
if wlan.status() != 3:
    raise RuntimeError('Network Connection has failed')
else:
    print('connected')
    oled.fill(0)
    oled.text("Connected",0,0)
    oled.text("O  O    ", 48, 25)
    oled.text(".__. ", 48, 45)
    oled.show()
    
    utime.sleep(0.5)
    oled.fill(0)
    oled.text("Connected",0,0)
    oled.text("^  ^    ", 48, 25)
    oled.text(".__. ", 48, 45)
    oled.show()
    
    utime.sleep(0.5)
    oled.fill(0)
    oled.text("Connected",0,0)
    oled.text("O  O    ", 48, 25)
    oled.text("\__/ ", 48, 45)
    oled.show()
    
    
while True:
    try:
        data=requests.get("http://api.open-notify.org/iss-now.json")
        location=data.json()
        print("ISS latitude={}".format(location['iss_position']['latitude']))
        print("ISS longitude={}".format(location['iss_position']['longitude']))
        oled.fill(0)
        oled.text(str("ISS lati={}".format(location['iss_position']['latitude'])),0,15)
        oled.text(str("ISS longi={}".format(location['iss_position']['longitude'])),0,35 )
        oled.show()
        data.close()

    except:
        print("could not connect (status =" + str(wlan.status()) + ")")
        if wlan.status() < 0 or wlan.status() >= 3:
            print("trying to reconnect...")
            wlan.disconnect()
            wlan.connect(ssid, password)
            if wlan.status() == 3:
                print('connected')
            else:
                print('connection failed')
    time.sleep(1)
    if button2.value() != 1:
        break
