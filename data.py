import django
import os
from datetime import datetime
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
django.setup()

import requests
from App.models import *



def get_data_as_API(city_name):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=658767b0ae936b022f59a69f44868419&units=metric"      
        response = requests.get(url)
        result = response.json()

        if result["cod"] != "404" :
            print(city_name)
            temperatrue = round(result['main']['temp'])
            humidity = result["main"]["humidity"]
            weather = result["weather"][0]["main"]
            id = str(result["weather"][0]["id"])
            wind_speed = round(result["wind"]["speed"])
            location = result["name"] + ", "+ result["sys"]["country"]
            now = datetime.now()
            Weather.objects.create(
                temperatrue = temperatrue,
                humidity = humidity,
                weather = weather,
                wind_speed = wind_speed,
                location = location
            )
            return {
                    "id": id,
                    "temperatrue": temperatrue,
                    "humidity": humidity,
                    "weather": weather,
                    "wind_speed": wind_speed,
                    "location": location,
                    "create":now.strftime("%Y-%m-%d|%H:%M:%S"),
                    
                }
  

    except Exception as e:
        print(e)
    return [{
            "id": id,
            "temperatrue": temperatrue,
            "humidity": humidity,
            "weather": weather,
            "wind_speed": wind_speed,
            "location": location,
            "create":now.strftime("%H:%M:%S"),
            
                }]


if __name__=="__main__":
    get_data_as_API("Tehran")