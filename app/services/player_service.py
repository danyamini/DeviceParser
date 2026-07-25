from app.scraper.player_scraper import get_scraped_players
from app.repositories.player_repo import create_player

def sync_players():
    players = get_scraped_players()

    for nickname in players:
        create_player(nickname)

def sync_preview():
    players = get_scraped_players()
    return players