from fastapi import APIRouter
from app.repositories.player_repo import get_players, get_player
from pydantic import BaseModel
from app.db.session import SessionLocal
from app.domain.player import Player
from app.services.player_service import sync_players, sync_preview

class PlayerCreate(BaseModel):
    nickname: str

router = APIRouter()

# УБРАТЬ ПРИ ДЕПЛОИ
@router.get("/debug")
def debug():
    db = SessionLocal()
    players = db.query(Player).all()
    db.close()
    return players

@router.get("/")
def read_players():
    print("HIT ENDPOINT")
    players = get_players()
    return players

@router.get("/preview")
def preview_players():
    players = sync_preview()
    return players

@router.get("/{id}")
def read_player(player_id: int):
    print("HIT")
    player = get_player(player_id)
    return player


@router.post("/sync")
def sync():
    sync_players()
    return{"status": "Players synchrnoized"}