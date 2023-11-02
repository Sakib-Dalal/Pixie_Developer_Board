#import modules
import network
import socket
from time import sleep
from machine import Pin, I2C
import bme280
import utime 
from ssd1306 import SSD1306_I2C

ssid = 'Asus ROG Phone' #Your network name
password = 'sakib dalal' #Your WiFi password

#initialize I2C 
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        oled = SSD1306_I2C(128, 64, i2c)

        print('Waiting for connection...')
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
        utime.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    oled = SSD1306_I2C(128, 64, i2c)
    oled.fill(0)
    oled.text("Web IP: ", 0, 0)
    oled.text(str(ip),0,30)
    oled.show()
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(reading):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Pico W Weather Station</title>
            <meta http-equiv="refresh" content="10">
            </head>
            <body>
            <h1>Pixie Developer Board</h1>
            <h1>     O     O</h1>
            <h1></h1>
            <h1>      .___.</h1>
            <br>
            <p>{reading}</p>
            </body>
            </html>
            """
    return str(html)
    
def serve(connection):
    #Start a web server
    
    while True:
        bme = bme280.BME280(i2c=i2c)
        temp = bme.values[0]
        pressure = bme.values[1]
        humidity = bme.values[2]
        reading = 'Temperature: ' + temp +  '. Pressure: ' + pressure
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)       
        html = webpage(reading)
        client.send(html)
        client.close()
        if button2.value() != 1:
            break

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
    