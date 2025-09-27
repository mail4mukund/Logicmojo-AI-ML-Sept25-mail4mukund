import requests

#print("Enter the URL of the JSON resource:")

req=requests.get('http://api.open-notify.org/astros.json')
print(req.json())

print("Enter your city name\n")
city=input()
url='http://api.weatherapi.com/v1/current.json?key=e9fe7ec5c7d24f86a55160352250209&q='+city+'&aqi=no'
req=requests.get(url)  
data=req.json()
print(data)
print("City: \t"+ data.get('location').get('name') + "\n Temperature: \t"+str(data.get('current').get('temp_c')))
print("Time Zonne: \t"+ data.get('location').get('tz_id') + "\n Is Day Now: \t"+str(data.get('current').get('is_day')))
