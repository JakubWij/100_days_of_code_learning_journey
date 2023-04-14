import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

SPOTIPY_CLIENT_ID = config['DEFAULT']['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = config['DEFAULT']['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = "http://example.com/localhost"
users_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD ")
# users_date = "2000-08-10"
url = f"https://www.billboard.com/charts/hot-100/{users_date}/"
# spotipy authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"))
user_id = sp.current_user()["id"]

# creating soup
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# getting titles from soup
some_titles = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                                                     "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                                                     "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                                                     "u-max-width-230@tablet-only")
some_titles2 = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                                                      "u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 "
                                                                      "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 "
                                                                      "u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
all_titles = some_titles + some_titles2
all_titles_stripped = [title.getText().strip() for title in all_titles]

# creating uri list from spotipy
year = users_date.split("-")[0]
tracks_uri = []
for track in all_titles_stripped:
    full_track = sp.search(q=f"track: {track} year: {year}", limit=1, type="track")
    try:
        track_uri = full_track["tracks"]["items"][0]["uri"]
        tracks_uri.append(track_uri)
    except IndexError:
        print(f"{track} doesn't exist in Spotify. Skipped.")

# create playlist and add tracks
playlist_id = sp.user_playlist_create(user=user_id, name=f"{users_date} Billboard 100", public=False)
print(playlist_id)

sp.playlist_add_items(playlist_id=playlist_id["id"], items=tracks_uri)


