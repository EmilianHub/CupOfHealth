from dataclasses import dataclass

from dbConnection import engine, Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

@dataclass
class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(engine)
