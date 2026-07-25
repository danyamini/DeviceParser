import requests
from bs4 import BeautifulSoup

BASE_URL = "https://prosettings.net/lists/cs2/"

def fetch_cs2_players():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(BASE_URL, headers=headers)
    response.raise_for_status()
    return response.text

def parse_players(html: str):
    soup = BeautifulSoup(html, "html.parser")

    players = []

    for item in soup.select("#pro-list-table tbody tr"):
        name_tag= item.select_one("span.name a")

        if not name_tag:
            continue

        name = name_tag.get_text(strip=True)
        profile_url = name_tag["href"]

        players.append({
            "name":name,
            "profile_url":profile_url
        })

    return players

def get_players():
    html = fetch_cs2_players()
    return parse_players(html)

if __name__ == "__main__":
    players = get_players()
    print(players)