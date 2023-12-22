import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime 

led = Pin(4, Pin.OUT)
led.value(0)

button1 = Pin(3, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)

i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 200000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.text(">_",0,0)
    oled.show()
    utime.sleep(1)
    oled.fill(0)
    oled.text(">",0,0)
    oled.show()
    utime.sleep(1)
    if button1.value() != 1 and button2.value() != 1:
        oled.fill(0)
        oled.text(">_",0,0)
        oled.show()
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">W",0,0)
        oled.show()
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">We",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Wel",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Welc",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Welco",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Welcom",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Welcome ",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Welcome B",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Welcome Ba",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Welcome Bac",0,0)
        oled.show()
        
        utime.sleep(0.3)
        oled.fill(0)
        oled.text(">Welcome Back",0,0)
        utime.sleep(0.5)
        oled.text("^  ^    ", 48, 25)
        oled.text(".__.  ", 48, 45)
        oled.show()
        
        utime.sleep(1)
        break
    
