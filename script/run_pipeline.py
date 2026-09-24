from extract import extract_weather
from transform import transform_weather

if __name__=='__main__':
    raw_data = extract_weather()
    df = transform_weather(raw_data)
    print(df)   # uncommented