import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime 

led = Pin(4, Pin.OUT)
led.value(0)

on = Pin(2, Pin.IN, Pin.PULL_UP)
off = Pin(6, Pin.IN, Pin.PULL_UP)

button1 = Pin(3, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)

WIDTH  = 128                                          
HEIGHT = 32
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)                     
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    oled.fill(0)
    oled.text("LED: ", 35, 12)
    if on.value() != 1:
        oled.text(" ON", 65, 12)
        led.value(1)
    elif off.value() != 1:
        oled.text(" OFF", 60, 12)
        led.value(0)
    oled.show()
    if button1.value() != 1:
        oled.fill(0)
        oled.text("! LED Pin: 4",0,0)
        oled.show()
        utime.sleep(2)
        
    if button2.value() != 1:
        oled = SSD1306_I2C(128, 64, i2c)
        break