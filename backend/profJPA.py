from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, ForeignKey, Table

from chorobyJPA import Diseases
from dbConnection import engine, Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

association_table2 = Table(
    "profToChoroba",
    Base.metadata,
    Column("Id_profilaktyka", ForeignKey("profilaktyka.id_prof"), primary_key=True),
    Column("id_choroba", ForeignKey("choroby.id_choroba"), primary_key=True),
)


@dataclass
class Prof(Base):
    __tablename__ = 'profilaktyka'

    id_prof: Mapped[int] = mapped_column(primary_key=True)
    profilaktyka: Mapped[str] = mapped_column(nullable=True)
    choroba: Mapped[List[Diseases]] = relationship(secondary=association_table2)

    def repr(self) -> str:
        return f"prof(id={self.id_prof!r}, pofilaktyka={self.profilaktyka!r})"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(engine)