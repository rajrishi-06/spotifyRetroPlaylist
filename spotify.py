import requests
import json
import webbrowser
import os
from dotenv import load_dotenv

load_dotenv()

class Spotify:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.access_token = os.getenv("SPOTIFY_ACCESS_TOKEN", "")  # Default to empty string if not found
        self.refresh_token = os.getenv("SPOTIFY_REFRESH_TOKEN", "")
        self.playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")
        self.user_id = os.getenv("SPOTIFY_USER_ID")
        self.redirect_uri = "http://localhost:8888/callback"
        self.auth_url = "https://accounts.spotify.com/authorize"
        self.token_url = "https://accounts.spotify.com/api/token"
        self.scope = "playlist-modify-public playlist-modify-private"

    def get_auth_url(self):
        auth_url = f"{self.auth_url}?client_id={self.client_id}&response_type=code&redirect_uri={self.redirect_uri}&scope={self.scope}"
        return auth_url

    def authorize_user(self):
        print("Opening browser for authorization...")
        webbrowser.open(self.get_auth_url())
        code = input("Enter the code from the URL: ")
        return code

    def get_access_token(self, code):
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(self.token_url, data=data)
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens.get('access_token')
        self.refresh_token = tokens.get('refresh_token')
        print(f"Access Token: {self.access_token}")

    def refresh_access_token(self):
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(self.token_url, data=data)
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens.get('access_token')
        print(f"Refreshed Access Token: {self.access_token}")

    def __get_song_uris(self, song_titles):
        song_uris = []
        headers = {'Authorization': f'Bearer {self.access_token}'}
        for song in song_titles:
            params = {'q': song, 'type': 'track', 'limit': 1}
            response = requests.get(url="https://api.spotify.com/v1/search", params=params, headers=headers)

            if response.status_code == 200:
                song_data = response.json().get('tracks', {}).get('items', [])
                if song_data:
                    song_uri = song_data[0].get('uri')
                    song_uris.append(song_uri)
                else:
                    print(f"No match found for: {song}")
            else:
                print(f"Error searching for song: {song}. Status code: {response.status_code}")
        return song_uris

    def create_playlist(self, date):
        if not self.access_token:
            print("Access token missing, authenticating...")
            code = self.authorize_user()
            self.get_access_token(code)

        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        data = {
            "name": f"{date} Billboard 100",
            "description": f"100 top liked songs of era {date}",
            "public": False
        }
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(data))

        if response.status_code == 201:
            self.playlist_id = response.json().get('id')
            print(f"Playlist created successfully: {self.playlist_id}")
        else:
            print(f"Error creating playlist: {response.status_code}, {response.text}")

    def add_songs_to_playlist(self, songs):
        if not self.access_token:
            print("Access token missing, authenticating...")
            code = self.authorize_user()
            self.get_access_token(code)

        song_uris = self.__get_song_uris(songs)

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        for song_uri in song_uris:
            params = {
                "uris": [song_uri],
                "position": 0
            }
            response = requests.post(
                url=f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks",
                headers=headers,
                data=json.dumps(params)
            )
            if response.status_code != 201:
                print(f"Error adding songs to playlist. Status code: {response.status_code}, {response.text}")
                return False
        return True