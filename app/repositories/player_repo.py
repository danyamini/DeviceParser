from app.domain.player import Player
from app.db.session import SessionLocal

def save_player(player_data: dict):
    db = SessionLocal()

    player = db.query(Player).filter(
        Player.profile_url == player_data["profile_url"]
    ).first()

    if player:
        player.nickname = player_data["nickname"]
        player.mouse = player_data["mouse"]
        player.monitor = player_data["monitor"]
        player.mousepad = player_data["mousepad"]
        player.keyboard = player_data["keyboard"]
        player.headset = player_data["headset"]

    else:
        player = Player(
            nickname=player_data["nickname"],
            profile_url=player_data["profile_url"],
            mouse=player_data["mouse"],
            monitor=player_data["monitor"],
            mousepad=player_data["mousepad"],
            keyboard=player_data["keyboard"],
            headset=player_data["headset"]
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