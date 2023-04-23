from dataclasses import dataclass
from typing import List

from sqlalchemy import ForeignKey

from wojeJPA import Wojewodztwa
from dbConnection import engine, Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column


@dataclass
class Miasta(Base):
    __tablename__ = "miasto"

    id: Mapped[int] = mapped_column(primary_key=True)
    woj_id: Mapped[int] = mapped_column(ForeignKey(Wojewodztwa.id))
    wojewodztwa: Mapped[Wojewodztwa] = relationship()
    nazwa: Mapped[str] = mapped_column(nullable=True, unique=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.table.columns}


Base.metadata.create_all(engine)