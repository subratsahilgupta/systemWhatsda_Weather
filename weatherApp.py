import requests
import json
from gtts import gTTS
import os

from datetime import date,datetime
todayTime = str(datetime.now())
formatted_time = todayTime.replace(" ", "_").replace(":", "-").replace(".", "--")

param = '''
        "location": {
                        "name": 
                        "region": ,
                        "country": ,
                        "lat": ,
                        "lon": ,
                        "tz_id": ,
                        "localtime_epoch": ,
                        "localtime": "
                    },
        
        "current": {
                    "last_updated_epoch": ,
                    "last_updated":,
                    "temp_c": ,
                    "temp_f": ,
                    "is_day":,
                    "condition": {
                                    "text": ",
                                    "icon": ,
                                    "code":
                                 },
                    "wind_mph": ,
                    "wind_kph": ,
                    "wind_degree": ,
                    "wind_dir": ,
                    "pressure_mb": ,
                    "pressure_in": ,
                    "precip_mm": ,
                    "precip_in": ,
                    "humidity":,
                    "cloud": ,
                    "feelslike_c": ,
                    "feelslike_f":,
                    "vis_km": 16,
                    "vis_miles":,
                    "uv":,
                    "gust_mph": ,
                    "gust_kph": "
                    
                    '''
def weather(firstKey, secondKey):
    try:
        return str(wDict[firstKey][secondKey])
    except KeyError:
        return False


def url(cityName, key = "185d4c5d7848422493644620241304"):
    return f"https://api.weatherapi.com/v1/current.json?key={key}&q={cityName}%27"

city = input("Enter the city name: ") 
print("@@@@@@\tTo get your own API key signup at {https://www.weatherapi.com/} and copy the FREE API key you have been provided below\t@@@@@@")

myKey = input("Enter your own api key if you have one or else enter continue: ")
if myKey == "continue":
    urlAdd = url(city)
else:
    urlAdd = url(city,myKey)
r = requests.get(urlAdd)
wDict = json.loads(r.text)


while True:

    print(f"what do you want to know about ths {city}")
    print(param)

    firstParam = input("Enter First Key: ")
    secondParam = input("Enter Second Key: ")

    speech = weather(firstParam,secondParam)

    if speech:
        tts = gTTS(speech)
        tts.save(f"{city}weather{formatted_time}.mp3")
        os.system(f"start {city}weather{formatted_time}.mp3")
        exit()
    else:
        print("key not found...Try again")
        