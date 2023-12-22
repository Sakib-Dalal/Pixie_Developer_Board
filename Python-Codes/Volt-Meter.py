import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime 

led = Pin(4, Pin.OUT)
led.value(0)


def pico_volt_main():
    # set up analog input on pin GP26
    adc = machine.ADC(26)

# set up serial communication at 9600 baud
#uart = machine.UART(0, 9600)

    i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 200000)
    oled = SSD1306_I2C(128, 32, i2c)

    button1 = Pin(3, Pin.IN, Pin.PULL_UP)
    button2 = Pin(7, Pin.IN, Pin.PULL_UP)

    while True:
    # read the voltage on GP26
        voltage = adc.read_u16() * 3.7 / 65535.0
    # print the voltage to the serial monitor
    #uart.write("Voltage: {:.2f} V\n".format(voltage))
        print(voltage)
        oled.fill(0)
        oled.text(" Voltage", 28, 0)
        oled.text(str(voltage) + " V", 28, 15)# ("text", x, y)
        oled.show()
    # wait for 1 second before taking the next measurement
        utime.sleep(1)
#     if right.value()!=0 and left.value()!=0 and button1.value()!=0 and button2.value()!=0:
#         # exit the loop
#         break
        if button1.value()!=1:
            oled.fill(0)
            oled.text("! Pin No: GP26",0,0)
            oled.show()
            utime.sleep(2)
            
        if button2.value()!= 1:
            oled = SSD1306_I2C(128, 64, i2c)
            break
    
if __name__ == "__main__":
    pico_volt_main()