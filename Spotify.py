import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

print("**Welcome to Spotify search . Search for the Artist and get their top Tracks**")
artist = input("Enter artist name :")
scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='539ac850801842a3aea49000c4078ca2', client_secret= '65bc32decdfa4606a10b4e386f8898c1', redirect_uri='http://localhost:9000'
, scope=scope))

response = requests.get("http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6")
print(response.status_code)
print(response.json())


results = sp.current_user_recently_played()

for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

track = input("enter an artist number to get thier top 3 tracks :")

print("happy coding !")
