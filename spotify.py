import requests
import base64
import os

class Spotify():

    def __init__(self):
        self.token = self.retrieve_token()
        self.max_recs = 5
    

    def retrieve_token(self):
        token_url = "https://accounts.spotify.com/api/token"
        id_secret = f"{os.environ['SPOTIFY_CLIENT_ID']}:{os.environ['SPOTIFY_CLIENT_SECRET']}"
        print(id_secret)
        id_secret_bytes = id_secret.encode("utf-8")
        id_secret_encoded = base64.b64encode(id_secret_bytes)
        id_secret_base64 = id_secret_encoded.decode('ascii')

        body = {
            "grant_type": "client_credentials"
        }
        headers = {
            "Authorization": f"Basic {id_secret_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(
            token_url,
            headers=headers,
            data=body
        )

        return response.json()["access_token"]
    
    def create_music_search(self, moods):
        search_url = "https://api.spotify.com/v1/search"
        query_payload = {}
        playlist_results = []
        for mood in moods:
            types_list = ["playlist"]
            query_payload = {
                "q": mood,
                "type": types_list
            }
            headers = {
                "Authorization": f"Bearer {self.token}"
            }
            response = requests.get(
                search_url, 
                params=query_payload, 
                headers=headers
                ).json()
            
            return response
            
            # count = 0
            # for item in playlist_search_results:
            #     playlist_item = {
            #         "name": item["name"]
            #     }
            
            # count = 0
            # for item in response["items"]:
            #     playlist_item = {
            #         "name": item["name"],
            #         "tracks": item["tracks"],
            #         "images": item["images"],
            #         "uri": item["uri"]
            #     }
            #     playlist_results.append(playlist_item)
            #     count += 1
            #     if count == self.max_recs:
            #         break

            # what to retrieve from the playlist object
            '''
            playlist tracks
            playlist uri
            playlist name
            playlist images
            '''


        return playlist_results

        
    
