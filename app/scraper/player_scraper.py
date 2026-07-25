import requests
from bs4 import BeautifulSoup

BASE_URL = "https://prosettings.net/lists/cs2/"

MOUSE_INDEX = 4
MONITOR_INDEX = 10
MOUSEPAD_INDEX = 16
KEYBOARD_INDEX = 17
HEADSET_INDEX = 18

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
        name_tag = item.select_one("span.name a")

        if not name_tag:
            continue

        nickname = name_tag.get_text(strip=True)
        profile_url = name_tag["href"]

        cells = item.select("td")
        mouse = cells[MOUSE_INDEX].get_text(strip=True) or None
        monitor = cells[MONITOR_INDEX].get_text(strip=True) or None
        mousepad = cells[MOUSEPAD_INDEX].get_text(strip=True) or None
        keyboard = cells[KEYBOARD_INDEX].get_text(strip=True) or None
        headset = cells[HEADSET_INDEX].get_text(strip=True) or None

        players.append({
            "nickname":nickname,
            "profile_url":profile_url,
            "mouse":mouse,
            "monitor":monitor,
            "mousepad":mousepad,
            "keyboard":keyboard,
            "headset":headset
        })

    return players

def get_scraped_players():
    html = fetch_cs2_players()
    return parse_players(html)

if __name__ == "__main__":
    players = get_scraped_players()
    print(players)