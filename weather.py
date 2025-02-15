import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q='
city = 'Berkeley'
state = 'CA'
country = 'USA'
apikey = '0d8e20b8b70a9296d4cbaa2816dbdecc'

query = '{},{},{}&appid={}'.format(city,state,country,apikey)
request = url + query
result = requests.get(request)
data = result.json()

def weather():
  weather = data['weather'][0]['main']  
  return weather

def wid():
  weatherid = data['weather'][0]['id']
  return weatherid

def temperature():
  degree_sign = u"\N{DEGREE SIGN}"
  tempC = str(round((data['main']['temp'] - 273.15),1))+degree_sign+"C"
  return tempC

def sunrise():
  utcsunrise = data['sys']['sunrise']
  return utcsunrise

def sunset():
  utcsunset = data['sys']['sunset']
  return utcsunset
