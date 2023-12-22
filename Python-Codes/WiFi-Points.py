import time
import machine
import network
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import urequests 

WIDTH  = 128                                          
HEIGHT = 64
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)


wlan=network.WLAN(network.STA_IF)
wlan.active(True)
while True:
    accesspoints = wlan.scan()
    for ap in accesspoints:
            print("ssid = {}".format(ap[0]))
            oled.fill(0)
            oled.text("ssid =",0,0)
            oled.text(str(ap[0]),0,20)
            oled.show()
    if button2.value() != 1:
            break
