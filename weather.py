import requests

i=0
city = input("Name of the city")
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=0c42f7f6b53b244c78a418f4f181282a' .format(city)


json_data =requests.get(url).json()
data_new=json_data['weather'][0]["main"] ,json_data['weather'][0]["description"]

for i in  data_new:
	print (i)
