import pandas as pd
from datetime import datetime



def transform_weather(raw_data):
    records = []

    for data in raw_data:
        record = {
            "name": data["name"],
            "country": data["sys"]["country"],
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather_description": data["weather"][0]["description"],
            "reading_time": datetime.fromtimestamp(data["dt"])
        }
        records.append(record)

    return pd.DataFrame(records)

