import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # store your key in env variable
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str):
    """Fetch weather data from OpenWeather API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # temperature in Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None
