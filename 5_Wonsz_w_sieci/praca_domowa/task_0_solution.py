from dataclasses import dataclass

import requests


@dataclass
class Weather:
    longitude: float
    latitude: float
    temperature: float
    feels_like: float
    pressure: int
    humidity: int
    clouds: int


def get_weather_for_point(longitude: float, latitude: float) -> Weather:
    query_params = {
        "appid": "86f800c5c5ddaab87f14095935de1c79",
        "exclude": "minutely,hourly,daily,alerts",
        "units": "metric",
        "lon": longitude,
        "lat": latitude,
    }

    r = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall", params=query_params
    )
    data = r.json()
    current = data["current"]

    return Weather(
        longitude=longitude,
        latitude=latitude,
        temperature=current["temp"],
        feels_like=current["feels_like"],
        pressure=current["pressure"],
        humidity=current["humidity"],
        clouds=current["clouds"],
    )


if __name__ == "__main__":
    print(get_weather_for_point(20, 30))
