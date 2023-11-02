
import urequests
import ujson
import machine
import network
ssid = 'Asus ROG Phone'
password = 'sakib dalal'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDhsh-pAuno9dWONXgNngmHAJKloXuEdlM'
headers = {'Content-type': 'application/json'}
data = {}
response = urequests.post(url, headers=headers, json=data)
json_data = ujson.loads(response.text)
print(json_data)
latitude = json_data['location']['lat']
longitude = json_data['location']['lng']
print('Latitude:', latitude)
print('Longitude:', longitude)
