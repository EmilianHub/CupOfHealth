from dataclasses import dataclass

from sqlalchemy import Column, Enum

from tagGroup import TagGroup
from dbConnection import engine, Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


@dataclass
class Patterns(Base):
    __tablename__ = 'chatbot_patterns'

    id: Mapped[int] = mapped_column(primary_key=True)
    pattern: Mapped[str] = mapped_column(nullable=True)
    pattern_group = Column(Enum(TagGroup, name="tag_group"))

    def __repr__(self) -> str:
        return f"Patterns(id={self.id!r}, pattern={self.pattern!r}, pattern_group={self.pattern_group!r})"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(engine)