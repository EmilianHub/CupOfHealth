from dataclasses import dataclass
from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from dbConnection import engine, Base
from patternsJPA import Patterns
from tagGroup import TagGroup

association_table = Table(
    "patterns_responses",
    Base.metadata,
    Column("pattern_id", ForeignKey("chatbot_patterns.id"), primary_key=True),
    Column("response_id", ForeignKey("chatbot_responses.id"), primary_key=True),
)


@dataclass
class Responses(Base):
    __tablename__ = 'chatbot_responses'

    id: Mapped[int] = mapped_column(primary_key=True)
    response: Mapped[str] = mapped_column(nullable=True)
    response_group: Mapped[TagGroup] = mapped_column(nullable=False)

    pattern: Mapped[List[Patterns]] = relationship(secondary=association_table)

    def __repr__(self) -> str:
        return f"Responses(id={self.id!r}, response={self.response!r}, response_group={self.response_group!r}, pattern={self.pattern!r})"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)

