from app.db.base import Base
from app.db.session import engine

from app.domain.player import Player

Base.metadata.create_all(bind=engine)