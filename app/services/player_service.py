from app.scraper.player_scraper import get_players
from app.repositories.player_repo import create_player

def sync_players():
    players = get_players()

    for nickname in players:
        create_player(nickname)