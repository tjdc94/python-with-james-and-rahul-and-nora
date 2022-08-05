import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import json 

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    s = sp.search("Sweet Caroline", type='track', limit=1)

    a = sp.audio_analysis('spotify:track:62AuGbAkt8Ox2IrFFb8GKV')
    # print(json.dumps(a,indent=2))


    af = sp.audio_features(tracks=['spotify:track:62AuGbAkt8Ox2IrFFb8GKV'])
    print(json.dumps(af,indent=2))





if __name__ == "__main__":
    main()

#'spotify:track:62AuGbAkt8Ox2IrFFb8GKV'