from app.scraper.player_scraper import get_scraped_players
from app.repositories.player_repo import save_player

def sync_players():
    players = get_scraped_players()

    for player in players:
        save_player(player)

def sync_preview():
    players = get_scraped_players()
    return players