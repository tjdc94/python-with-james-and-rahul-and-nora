import requests
from tabulate import tabulate

response = requests.get("https://api.tvmaze.com/shows")
shows = response.json()

def display_shows_table(shows):
    table = [
        [
            idx + 1,
            s["name"],
            ", ".join(s["genres"]),
            s["runtime"],
            s["rating"]["average"],
            s["status"],
        ]
        for idx, s in enumerate(shows) 

    headers = ["#", "Name", "Genres", "Runtime", "Rating", "Status"]
    print(tabulate(table, headers=headers, tablefmt="orgtbl"))

def recommend_shows(genres=[], minimum_rating=0, status=None):
    candidates = []
    for show in shows:
        show_genres = set([genre.lower() for genre in show["genres"]])
        matches = 0
        for genre in genres:
            if genre.lower() in show_genres:
                matches += 1
        if (
            matches == len(genres)
            and show["rating"]["average"]
            and show["rating"]["average"] >= minimum_rating
            and (status is None or show["status"].lower() == status.lower())
        ):
            candidates.append(show)
    candidates = sorted(candidates, key=lambda d: d["rating"]["average"], reverse=True)
    return candidates


display_shows_table(recommend_shows(status="running"))