from app.domain.player import Player
from app.db.session import SessionLocal

def create_player(player_data: dict):
    db = SessionLocal()

    player = Player(
        nickname = player_data["name"],
        profile_url=player_data["profile_url"]
    )

    db.add(player)
    db.commit()
    db.refresh(player)

    db.close()
    
    return player

def get_players():
    db = SessionLocal()

    players = db.query(Player).all()

    db.close()
    return players

def get_player(player_id: int):
    db = SessionLocal()

    player = db.query(Player).filter(Player.id == player_id).first()

    db.close()
    return player.nickname