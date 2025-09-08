from rich import print
from rich.table import Table


def display_weather(data: dict):
    """
    Display weather information in a formatted table using Rich.

    Args:
        data (dict): A dictionary containing weather details
                     (temperature, humidity, wind, etc.)
                     from the OpenWeather API response.

    The function creates a styled table with parameters such as
    temperature, feels-like temperature, humidity, weather description,
    and wind speed, and prints it to the console.
    """

    table = Table(title=f"Weather in {data['name']}, {data['sys']['country']}")

    table.add_column("Parameter", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Temperature", f"{data['main']['temp']}°C")
    table.add_row("Feels Like", f"{data['main']['feels_like']}°C")
    table.add_row("Humidity", f"{data['main']['humidity']}%")
    table.add_row("Weather", data["weather"][0]["description"].title())
    table.add_row("Wind Speed", f"{data['wind']['speed']} m/s")

    print(table)
