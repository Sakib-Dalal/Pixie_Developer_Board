# Display Image & text on I2C driven ssd1306 OLED display
import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import machine
import utime

button2 = Pin(7, Pin.IN, Pin.PULL_UP)
     
TempSensor = machine.ADC(4)
WIDTH  = 128                                          
HEIGHT = 64
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)       
conversion_factor = 3.3 / 65535                
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  
while True:
    data = TempSensor.read_u16() * conversion_factor  
    temperature = 27-(data-0.706)/0.001721 
    oled.fill(0) 
    oled.text("Temperature: ", 0, 0)
    oled.text(str(round(temperature,1))+" *C",38,28)

    oled.show()
        
    if button2.value()!= 1:
        break
        
# if __name__ == "__main__":
#     pico_temp_main()