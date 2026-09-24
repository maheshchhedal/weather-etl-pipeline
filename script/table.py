from config import engine
from sqlalchemy import text


def create_tables():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS cities (
                city_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL UNIQUE,
                country VARCHAR(10),
                lat DECIMAL(9,6),
                lon DECIMAL(9,6)
            )
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS weather_readings (
                reading_id INT AUTO_INCREMENT PRIMARY KEY,
                city_id INT NOT NULL,
                reading_time DATETIME NOT NULL,
                temperature FLOAT,
                humidity FLOAT,
                wind_speed FLOAT,
                weather_description VARCHAR(255),
                FOREIGN KEY (city_id) REFERENCES cities(city_id),
                UNIQUE KEY unique_reading (city_id, reading_time)
            )
        """))
        conn.commit()
        print("Tables created (or already exist).")

if __name__ == "__main__":
    create_tables()