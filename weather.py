import requests
import os

class Weather:

    def __init__(self):
        self.weather_moods = {
            "Sunny": "Cheerful, uplifting, energizing",
            "Cloudy": "Contemplative, gloomy, calm",
            "Overcast": "Contemplative, gloomy, calm",
            "Rain": "Reflective, melancholic, cozy",
            "Showers": "Unpredictable, dynamic, refreshing",
            "Scattered Rain": "Unpredictable, dynamic, refreshing",
            "Thunderstorm": "Intense, dramatic, electric",
            "Snowy": "Peaceful, magical, sometimes isolating",
            "Foggy": "Mysterious, eerie, quiet",
            "Windy": "Wild, chaotic, refreshing",
            "Severe Weather": "Anxious, thrilling, ominous"
        }

        self.weather_moods = {
            ""
        }

    def get_weather(self):
        base_url = "http://api.weatherapi.com/v1"
        current_weather = "/current.json"
        query_params = {
            "q": "02148",
            "key": os.environ["WEATHER_KEY"]
        }

        response = requests.get(
            f"{base_url}{current_weather}",
            params=query_params
        )

        return response.json()
    
    def get_conditions(self):
        weather_response = self.get_weather()
        current_conditions = weather_response["current"]["condition"]
        return current_conditions
    
    def get_moods(self, conditions):
        try:
            return self.weather_moods[conditions["text"]]
        except:
            return []