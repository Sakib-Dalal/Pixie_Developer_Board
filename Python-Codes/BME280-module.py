# Import necessary modules
import machine
from machine import Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C
import bme280
import utime 

# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
# Initialize BME280 sensor
bme = bme280.BME280(i2c=i2c)


button1 = Pin(3, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)

while True:
    # Read sensor data
    bme = bme280.BME280(i2c=i2c)
    temp = bme.values[0]
    pressure = bme.values[1]
    humidity = bme.values[2]

    # Print sensor readings
    reading = 'Temp: {} Pressure: {}'.format(temp, pressure)
    temp = 'Temp: ' + temp
    pressure = 'Pres: ' + pressure
    print(reading)

    # Wait for 10 seconds
    sleep(0.5)
    oled = SSD1306_I2C(128, 64, i2c)
    oled.fill(0)
    #oled.text("BME280-Module: ", 0, 3)
    oled.text((temp),0,20)
    oled.text((pressure),0,40)
    oled.show()
    # wait for 1 second before taking the next measurement
    utime.sleep(1)

    if button2.value() != 1:
        break