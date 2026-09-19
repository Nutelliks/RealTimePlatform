from __future__ import annotations

import enum
import uuid

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.models.base import Base, TimeStampMixin, UUIDPKMixin


class RoomType(enum.StrEnum):
    GROUP = "group"
    STREAM = "stream"
    DM = "dm"


class Room(UUIDPKMixin, TimeStampMixin, Base):
    __tablename__ = "room"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[RoomType] = mapped_column(
        SAEnum(RoomType, name="room_type", native_enum=False, create_constraint=True),
        nullable=False,
    )
    is_private: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    hash_password: Mapped[str | None] = mapped_column(String(255), nullable=True)
    owner_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), index=True, nullable=False
    )
