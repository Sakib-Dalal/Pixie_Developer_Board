
import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import machine
import utime

led = Pin(4, Pin.OUT)
led.value(0)

button1 = Pin(3, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)
info_button = Pin(2, Pin.IN, Pin.PULL_UP)

trigger = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN)
def distance():
    timepassed=0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    return timepassed
 
WIDTH  = 128                                          
HEIGHT = 32
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)                     
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  
while True:
    oled.fill(0)
    measured_time = distance()     
    distance_cm = (measured_time * 0.0343) / 2
    
    oled.fill(0) 
    oled.text("Distance ", 35, 0)
    oled.text(str(round(distance_cm,1))+" cm",42,15)
    oled.text(" |------------|",0,20)
    
    print("Distance: " + str(round(distance_cm,1)) + " cm")
    oled.show()
    
    if info_button.value() == 0:
        oled.fill(0)
        oled.text("trigger pin: 17",0,0)
        oled.text("echo pin: 16",0,10)

        oled.show()
        utime.sleep(2)
    
    if button2.value() == 1:
        led.value(0)
    if button2.value() == 0:
        led.value(1)
    if button1.value() != 1:
        oled = SSD1306_I2C(128, 64, i2c)
        break
    
    