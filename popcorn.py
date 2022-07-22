import requests
from pprint import pprint

response = requests.get("https://api.tvmaze.com/shows")
response_json = response.json()

shows = response_json
#pprint(list(show.keys()))
#show_name = show["name"]
#show_rating = show["rating"]["average"]
        
#pprint(show_name)
#pprint(show_rating)

#shows_above_7 = []

# for show in shows:
#     show_rating = show["rating"]["average"]
#     if show_rating != None and show_rating >= 7:
#         shows_above_7.append(show)

#pprint(shows_above_7[:2])

def is_rated_above_7(show: dict) -> bool:
    show_rating = show["rating"]["average"]
    return show_rating != None and show_rating >= 7

#pprint(is_rated_above_7(shows[0]))

#shows_above_7 = filter(is_rated_above_7, shows) #takes a boolean function and a iterable. Filter allows you to detach the iteration and the filtering

shows_above_7 = [show["name"] for show in shows if is_rated_above_7(show)] #list comprehension

pprint(shows_above_7)

