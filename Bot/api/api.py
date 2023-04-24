import requests
import os

async def get_weather(city):
    token = os.environ.get("token_weather")
    chords = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={token}").json()
    try:
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={chords[0]['lat']}&lon={chords[0]['lon']}&appid={token}&units=metric").json()
        print(weather)
        if chords[0]['local_names']:
            return weather, chords[0]['local_names']
        return False
    except:
        return False

async def convert(cur1, cur2, quantity):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur2}&from={cur1}&amount={quantity}"
    headers= {
        "apikey": os.environ.get("token_converter")
    }

    response = requests.request("GET", url, headers=headers).json()
    return response