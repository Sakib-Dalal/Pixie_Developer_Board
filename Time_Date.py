import network
import ssd1306
import utime

# Wi-Fi Credentials
SSID = "Asus ROG Phone"
PASSWORD = "sakib dalal"

# Initialize Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

# Initialize OLED display
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
display = ssd1306.SSD1306_I2C(128, 32, i2c)

# Main loop
while True:
    # Check if Wi-Fi is connected
    if wifi.isconnected():
        # Get current time
        current_time = utime.localtime()

        # Format date and time strings
        date_string = "{:02d}/{:02d}/{:04d}".format(current_time[2], current_time[1], current_time[0])
        time_string = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])

        # Print date and time to OLED display
        display.fill(0)
        display.text(date_string, 0, 0)
        display.text(time_string, 0, 10)
        display.show()

    # Wait for 1 second
    utime.sleep(1)
