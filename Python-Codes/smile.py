import machine
from machine import Pin

import ssd1306
from ssd1306 import SSD1306_I2C

import utime

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
#oled = SSD1306_I2C(128, 64, i2c)

button1 = Pin(3, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)

while True:
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("x    x", 43, 5)
    oled.text(" ____", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("-    -    ", 43, 5)
    oled.text(" ____  ", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("O    o    ", 43, 5)
    oled.text(".____  ", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("o   O    ", 43, 5)
    oled.text("____.  ", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("O   O    ", 43, 5)
    oled.text(".___.  ", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("O   O    ", 43, 5)
    oled.text("\___/  ", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("-   -    ", 43, 5)
    oled.text("\___/  ", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("O   O    ", 43, 5)
    oled.text("\___/  ", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("O   ^   ", 43, 5)
    oled.text("\___/ ", 43, 20)
    oled.show()

    oled.fill(0)
    utime.sleep(0.5)
    oled.text("O   O   ", 43, 5)
    oled.text("\___/ ", 43, 20)
    oled.show()
    
    oled.fill(0)
    utime.sleep(0.5)
    oled.text("-   -    ", 43, 5)
    oled.text("\___/  ", 43, 20)
    oled.show()
    
    if button2.value() != 1:
        break