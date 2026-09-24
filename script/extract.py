import requests
import os
import json
from datetime import date
from dotenv import load_dotenv
from city import cities

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"


def extract_weather():
    today = date.today().isoformat()
    raw_folder = f"raw/{today}"
    os.makedirs(raw_folder, exist_ok=True)

    for city in cities:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(URL, params=params)

        if response.status_code == 200:
            data = response.json()

            file_name = city.split(",")[0].lower().replace(" ", "_")
            file_path = f"{raw_folder}/{file_name}.json"

            with open(file_path, "w") as f:
                json.dump(data, f)

            print(f"Saved: {file_path}")
        else:
            print(f"Error for {city}: {response.status_code} - {response.text}")


if __name__ == "__main__":
    extract_weather()