from fastapi import FastAPI
from app.api.routes import players

app = FastAPI()

app.include_router(players.router, prefix="/players")

@app.get("/")
def root():
    return {"status": "ok"}