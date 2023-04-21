from dataclasses import dataclass
from typing import List

from dbConnection import engine, Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from miastaJPA import Miasta

@dataclass
class Woje(Base):
    __tablename__ = 'woje'

    id: Mapped[int] = mapped_column(primary_key=True)
    nazwa: Mapped[str] = mapped_column(nullable=True)
    miasta: Mapped[List[Miasta]]=relationship(back_populates=Miasta.woje)


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(engine)