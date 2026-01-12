from weather import Weather
from spotify import Spotify
from fastapi import FastAPI

app = FastAPI()

@app.get("/get-music/")
def get_weather():
    weather = Weather()
    spotify = Spotify()

    moods = weather.get_mood_keywords()
    search_results = spotify.search_music(moods)

if __name__ == "__main__":
    weather = Weather("02148")
    spotify = Spotify()

    moods = weather.get_mood_keywords()
    search_results = spotify.search_music(moods)

    