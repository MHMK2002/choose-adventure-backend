from __future__ import annotations

from sqlalchemy import JSON, Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from db.database import Base


class Story(Base):
    __tablename__ = 'stories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    session_id: Mapped[str] = mapped_column(String, index=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    nodes: Mapped[list[StoryNode]] = relationship('StoryNode', back_populates='story')


class StoryNode(Base):
    __tablename__ = 'story_nodes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    story_id: Mapped[int] = mapped_column(Integer, ForeignKey('stories.id'), index=True)
    content: Mapped[str] = mapped_column(String)
    is_root: Mapped[bool] = mapped_column(Boolean, default=False)
    is_ending: Mapped[bool] = mapped_column(Boolean, default=False)
    is_winning_ending: Mapped[bool] = mapped_column(Boolean, default=False)
    options: Mapped[list[dict]] = mapped_column(JSON, default=list)

    story: Mapped[Story | None] = relationship('Story', back_populates='nodes')
