import argparse
from weather_cli.weather import get_weather
from weather_cli.utils import display_weather


def main():
    parser = argparse.ArgumentParser(description="Fetch live weather data for a given city using OpenWeather API.")

    parser.add_argument("--city", type=str, required=True, help="Name of the city to fetch weather for")

    args = parser.parse_args()

    city = args.city
    data = get_weather(city)

    if data:
        display_weather(data)
    else:
        print("Could not fetch weather data. Check your city name or API key.")


if __name__ == "__main__":
    main()
