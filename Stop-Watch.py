import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime 

led = Pin(4, Pin.OUT)
led.value(0)

# Set up the OLED display
i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 200000)
oled = SSD1306_I2C(128, 32, i2c)

# Set up the button pins
start_stop_button = Pin(2, Pin.IN, Pin.PULL_UP)
reset_button = Pin(6, Pin.IN, Pin.PULL_UP)

button2 = Pin(7, Pin.IN, Pin.PULL_UP)

# Set up initial variables
start_time = 0
stop_time = 0
running = False
elapsed_time = 0

# Main loop
while True:
    # Check if the start/stop button has been pressed
    if start_stop_button.value() == 0:
        if not running:
            # If the stopwatch is not currently running, start it
            start_time = utime.ticks_ms()
            running = True
        else:
            # If the stopwatch is currently running, stop it
            stop_time = utime.ticks_ms()
            elapsed_time += utime.ticks_diff(stop_time, start_time)
            running = False
    
    # Check if the reset button has been pressed
    if reset_button.value() == 0:
        # If the stopwatch is currently running, stop it before resetting
        if running:
            stop_time = utime.ticks_ms()
            elapsed_time += utime.ticks_diff(stop_time, start_time)
            running = False
        # Reset the elapsed time to 0
        elapsed_time = 0
    
    # Display the elapsed time on the OLED display
    oled.fill(0)
    oled.text("Stop Watch:", 25, 0)
    oled.text(str(elapsed_time // 1000) + " : " + str(elapsed_time % 1000), 45, 15)

    oled.show()
    
    # Delay for a short time to prevent the loop from running too quickly
    utime.sleep_ms(50)
    
    if button2.value()!= 1:
        oled = SSD1306_I2C(128, 64, i2c)
        break
    
