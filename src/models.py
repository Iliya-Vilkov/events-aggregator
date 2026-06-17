from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Event(Base):
    """Модель события."""

    __tablename__ = "events"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    place_id: Mapped[UUID] = mapped_column(UUID, nullable=False)
    event_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    number_of_visitors: Mapped[int] = mapped_column(nullable=False)
    changed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False)
    registration_deadline: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False)


class Place(Base):
    """Модель места проведения события."""

    __tablename__ = "places"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    seats_pattern: Mapped[str] = mapped_column(nullable=False)
