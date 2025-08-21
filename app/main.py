import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    params = {"key": API_KEY, "q": "paris", "aqi": "no"}
    response = requests.get(BASE_URL, params=params)
    data_response = response.json()
    return print(
        f"Performing request to Weather API for "
        f"city {data_response["location"]["name"]}...\n"
        f"{data_response["location"]["name"]}/"
        f"{data_response["location"]["country"]} "
        f"{data_response["location"]["localtime"]} "
        f"Weather: {data_response["current"]["temp_c"]}  "
        f"Celsius, {data_response["current"]["condition"]["text"]}"
    )


if __name__ == "__main__":
    get_weather()
