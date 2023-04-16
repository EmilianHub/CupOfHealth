from dataclasses import dataclass
from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from dbConnection import engine, Base
from objawyJPA import Symptoms

association_table = Table(
    "objawy_to_choroba",
    Base.metadata,
    Column("id_objawu", ForeignKey("objawy.id_objawy"), primary_key=True),
    Column("id_choroby", ForeignKey("choroby.id_choroba"), primary_key=True),
)


@dataclass
class Diseases(Base):
    __tablename__ = 'choroby'

    id_choroba: Mapped[int] = mapped_column(primary_key=True)
    choroba: Mapped[str] = mapped_column(nullable=True)

    objawy: Mapped[List[Symptoms]] = relationship(secondary=association_table)

    def __repr__(self) -> str:
        return f"Diseases(id={self.id_choroba!r}, choroba={self.choroba!r}, objawy={self.objawy!r})"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(engine)

