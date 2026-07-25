from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Player(Base):
    __tablename__ = 'players'

    id: Mapped[int] = mapped_column(primary_key=True)
    profile_url: Mapped[str] = mapped_column(String, unique=True)
    nickname: Mapped[str] = mapped_column(String)

    mouse: Mapped[str | None] = mapped_column(String, nullable=True)
    keyboard: Mapped[str | None] = mapped_column(String, nullable=True)
    monitor: Mapped[str | None] = mapped_column(String, nullable=True)
    mousepad: Mapped[str | None] = mapped_column(String, nullable=True)
    headset: Mapped[str | None] = mapped_column(String, nullable=True)