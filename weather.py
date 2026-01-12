import requests
import os
import constants


class Weather:

    def __init__(self, zipcode: str):
        self.zipcode = -1

    '''
    zip: Zip code entered by the user
    '''
    def get_weather(self) -> str:
        base_url = "http://api.weatherapi.com/v1"
        current_weather = "/current.json"
        query_params = {
            "q": self.zipcode,
            "key": os.environ["WEATHER_KEY"]
        }

        response = dict(requests.get(
            f"{base_url}{current_weather}",
            params=query_params
        ).json())

        condition_code = response["current"]["condition"]["code"]
        for condition in constants.WEATHER_CONDITIONS:
            if condition_code in constants.WEATHER_CONDITIONS[condition]:
                return condition

        return ""

    def get_mood_keywords(self) -> list[str]:
        weather_condition = self.get_weather()
        return constants.MOOD_KEYWORDS[weather_condition]