from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from db.database import Base

if TYPE_CHECKING:
    from models.story import Story


class StoryJob(Base):
    __tablename__ = 'story_jobs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    job_id: Mapped[str] = mapped_column(String, index=True, unique=True)
    session_id: Mapped[str] = mapped_column(String, index=True)
    theme: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    story_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('stories.id'), index=True, nullable=True)
    error: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    completed_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    story: Mapped[Story | None] = relationship('Story')