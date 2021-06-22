import requests
from datetime import datetime



City_ = input("City name: ")
api_ ="106f6f55895cc2540798bc4b56505470"


Link ="https://api.openweathermap.org/data/2.5/weather?q="+City_+"&appid="+api_


Get_Data= requests.get(Link)
Content_ = Get_Data.json()

hdty= Content_['main']['humidity']
dptn = Content_['weather'][0]['description']
Spd=Content_['wind']['speed']
Date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
Temptr = '%.2f'%((Content_['main']['temp'])-273.15)
Location= Content_['name']


fname=open("Shape_AI_Project.txt","w+")

fname.write("\nWeather Status in {} on {}".format(Location, Date_time))
fname.write("\n.......................................................")
fname.write("\nCity Name          :%s" %Location)
fname.write("\nTemperature        :%s Celsius" %Temptr)
fname.write("\nHumidity           :%s" %hdty)
fname.write("\nWind Speed         :%s" %Spd)
fname.write("\nDescription        :%s" %dptn)

fname.close()

fname=open("Shape_AI_Project.txt","r")
t_file=fname.read()
for a in t_file:
    print(a,end="")
fname.close()


