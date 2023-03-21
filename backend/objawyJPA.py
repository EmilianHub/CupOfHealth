from dataclasses import dataclass

from dbConnection import engine, Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


@dataclass
class Symptoms(Base):
    __tablename__ = 'objawy'

    id_objawy: Mapped[int] = mapped_column(primary_key=True)
    objawy: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"Symptoms(id={self.id_objawy!r}, objawy={self.objawy!r})"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(engine)