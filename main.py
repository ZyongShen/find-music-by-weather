from weather import Weather
from spotify import Spotify

if __name__ == "__main__":
    weather = Weather()
    spotify = Spotify()

    current_conditions = weather.get_conditions()
    print(current_conditions)
    weather_moods = weather.get_moods(current_conditions)

    playlists = spotify.create_music_search(weather_moods)
    print(playlists)

    