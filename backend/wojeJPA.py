from dataclasses import dataclass

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from dbConnection import engine, Base


@dataclass
class Wojewodztwa(Base):
    __tablename__ = 'wojewodztwo'

    id: Mapped[int] = mapped_column(primary_key=True)
    nazwa: Mapped[str] = mapped_column(nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.table.columns}


Base.metadata.create_all(engine)
