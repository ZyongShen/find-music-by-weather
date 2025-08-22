import requests
import base64
import os

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

token = response.json()["access_token"]

class Spotify():

    def __init__(self):
        self.token = ''
    

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

        self.token = response.json()["access_token"]
    
    