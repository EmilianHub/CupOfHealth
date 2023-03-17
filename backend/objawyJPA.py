from dbConnection import engine, Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Symptoms(Base):
    __tablename__ = 'objawy'

    id_objawy: Mapped[int] = mapped_column(primary_key=True)
    objawy: Mapped[str] = mapped_column(nullable=True)


Base.metadata.create_all(engine)