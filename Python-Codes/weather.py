import urequests
import network
import time
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Asus ROG Phone","sakib dalal")
openweather_api_key = "cd09c0349e916e068b5b80527b57cf9f"
 
# connect the network       
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)
 
# syncing the time
import ntptime
while True:
    try:
        ntptime.settime()
        print('Time Set Successfully')
        break
    except OSError:
        print('Time Setting...')
        continue
 
# init LCD

 
 
# Open Weather
TEMPERATURE_UNITS = {
    "standard": "K",
    "metric": "°C",
    "imperial": "°F",
}
 
SPEED_UNITS = {
    "standard": "m/s",
    "metric": "m/s",
    "imperial": "mph",
}
 
units = "metric"
 
def get_weather(city, api_key, units='metric', lang='en'):
    '''
    Get weather data from openweathermap.org
        city: City name, state code and country code divided by comma, Please, refer to ISO 3166 for the state codes or country codes. https://www.iso.org/obp/ui/#search
        api_key: Your unique API key (you can always find it on your openweather account page under the "API key" tab https://home.openweathermap.org/api_keys
        unit: Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default. More: https://openweathermap.org/current#data
        lang: You can use this parameter to get the output in your language. More: https://openweathermap.org/current#multi
    '''
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={lang}"
    print(url)
    res = urequests.post(url)
    return res.json()
 
def print_weather(weather_data):
    print(f'Timezone: {int(weather_data["timezone"] / 3600)}')
    sunrise = time.localtime(weather_data['sys']['sunrise']+weather_data["timezone"])
    sunset = time.localtime(weather_data['sys']['sunset']+weather_data["timezone"])
    print(f'Sunrise: {sunrise[3]}:{sunrise[4]}')
    print(f'Sunset: {sunset[3]}:{sunset[4]}')   
    print(f'Country: {weather_data["sys"]["country"]}')
    print(f'City: {weather_data["name"]}')
    print(f'Coordination: [{weather_data["coord"]["lon"]}, {weather_data["coord"]["lat"]}')
    print(f'Visibility: {weather_data["visibility"]}m')
    print(f'Weather: {weather_data["weather"][0]["main"]}')
    print(f'Temperature: {weather_data["main"]["temp"]}{TEMPERATURE_UNITS[units]}')
    print(f'Temperature min: {weather_data["main"]["temp_min"]}{TEMPERATURE_UNITS[units]}')
    print(f'Temperature max: {weather_data["main"]["temp_max"]}{TEMPERATURE_UNITS[units]}')
    print(f'Temperature feels like: {weather_data["main"]["feels_like"]}{TEMPERATURE_UNITS[units]}')
    print(f'Humidity: {weather_data["main"]["humidity"]}%')
    print(f'Pressure: {weather_data["main"]["pressure"]}hPa')
    print(f'Wind speed: {weather_data["wind"]["speed"]}{SPEED_UNITS[units]}')
    #print(f'Wind gust: {weather_data["wind"]["gust"]}{SPEED_UNITS[units]}')
    print(f'Wind direction: {weather_data["wind"]["deg"]}°')
    if "clouds" in weather_data:
        print(f'Cloudiness: {weather_data["clouds"]["all"]}%')
    elif "rain" in weather_data:
        print(f'Rain volume in 1 hour: {weather_data["rain"]["1h"]}mm')
        print(f'Rain volume in 3 hour: {weather_data["rain"]["3h"]}mm')
    elif "snow" in weather_data:
        print(f'Snow volume in 1 hour: {weather_data["snow"]["1h"]}mm')
        print(f'Snow volume in 3 hour: {weather_data["snow"]["3h"]}mm')    
 
 
while True:
    # get weather
    weather_data = get_weather('dubai', openweather_api_key, units=units)
    weather=weather_data["weather"][0]["main"]
    t=weather_data["main"]["temp"]
    rh=weather_data["main"]["humidity"]
 
    # get time
    hours=time.localtime()[3]+int(weather_data["timezone"] / 3600)
    mins=time.localtime()[4]
 
    # LCD print
    
 
    # shell print
    print_weather(weather_data)
 
    # refresh every 30s
    time.sleep(30)