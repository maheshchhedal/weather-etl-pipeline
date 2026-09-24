import requests
import os
from dotenv import load_dotenv
from city import cities

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"


def extract_weather():
    all_data = []

    for city in cities:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(URL, params=params)
        data = response.json()
        all_data.append(data)

    return all_data



if __name__ == "__main__":
    extract_weather()