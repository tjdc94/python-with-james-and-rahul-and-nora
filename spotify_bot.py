import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import json 

# def main():
#     sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

#     s = sp.search("Sweet Caroline", type='track', limit=1)

#     a = sp.audio_analysis('spotify:track:62AuGbAkt8Ox2IrFFb8GKV')
#     # print(json.dumps(a,indent=2))


#     af = sp.audio_features(tracks=['spotify:track:62AuGbAkt8Ox2IrFFb8GKV'])
#     print(json.dumps(af,indent=2))

def happy_scorer(features):
    """
    sort features based on happy score
    happy score will give weight to different audio features. e.g. 0.8 to Valence, 0.5 to danceability & 0.4 to energy
    """
    valence_weight = 0.47
    danceability_weight = 0.29
    energy_weight = 0.24
    assert valence_weight + danceability_weight + energy_weight == 1.0, 'All weights must sum up to 1'

    happy_score = [{'id': f['id'], 'score':(f['valence']*valence_weight + f['danceability']*danceability_weight + f['energy']*energy_weight)} for f in features]
    return happy_score

def get_songs_of_playlist(sp, playlist_id):
    songs = sp.playlist(playlist_id)
    song_ids = [song['track']['id'] for song in songs['tracks']['items']]
    return song_ids


#Next we need to get playlist ID

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    #s = sp.search("Happy", type='playlist', limit=1)
    #s = sp.search("Sad", type='playlist', limit=1)

    sad_id = '37i9dQZF1EIfqEXXMuoYtV'
    happy_id = '37i9dQZF1DWSf2RDTDayIx'

    happy_song_ids = get_songs_of_playlist(sp, happy_id)
    sad_song_ids = get_songs_of_playlist(sp, sad_id)

    audio_features = sp.audio_features(tracks=sad_song_ids)
    features = [{'id': af['id'], 'valence': af['valence'], 'energy': af['energy'], 'danceability': af['danceability'] }  for af in audio_features]
    #pprint(features)

    #pprint(happy_scorer(features))
    happy_list = sorted(happy_scorer(features), key = lambda song: song['score'], reverse = True)
    pprint(happy_list)


if __name__ == "__main__":
    main()


#'spotify:track:62AuGbAkt8Ox2IrFFb8GKV'