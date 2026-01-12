import requests
from dotenv import load_dotenv
import os

class Spotify():

    def __init__(self):
        load_dotenv()
        self.token = self._retrieve_token()


    def _retrieve_token(self):
        try:
            payload = {
                "grant_type": "client_credentials",
                "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
                "client_secret": os.getenv("SPOTIFY_CLIENT_SECRET")
            }
            url = "https://accounts.spotify.com/api/token"
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            response = requests.post(
                url=url,
                data=payload,
                headers=headers
            )
            return response.json().get("access_token")

        except Exception as e:
            raise Exception(str(e))

    def search_music(self, keywords: list[str]):
        url = "https://api.spotify.com/v1/search"
        search_string = ",".join(keywords) + " music"
        types = ["playlist", "album", "track"]
        params = {
            "q": search_string,
            "type": ",".join(types)
        }
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        result = {
            "albums": {},
            "playlists": {},
            "tracks": {}
        }


        try:
            response = requests.get(
                url,
                params=params,
                headers=headers
            )
            if response.status_code != 200:
                return "Search Failed"

            response_map = dict(response.json())
            # aspects to take --> first image, name, external_urls[spotify]
            # get 1 album, 1 track, 1 playlist
            for k in result.keys():
                print(k)
                print(response_map[k]["items"][0].keys())
                result[k] = {
                    "image": response_map[k]["items"][0]["album"]["images"][0]["url"] if k is "tracks" else response_map[k]["items"][0]["images"][0]["url"],
                    "external_link": response_map[k]["items"][0]["external_urls"]["spotify"],
                    "name": response_map[k]["items"][0]["name"]
                }

            print("line 71")
            return result


        except Exception as e:
            return {"error": f"Unexpected error occurred: {str(e)}"}
        
    
