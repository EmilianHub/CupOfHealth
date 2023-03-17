from dbConnection import engine, Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase


class Diseases(Base):
    __tablename__ = 'choroby'

    id_choroba: Mapped[int] = mapped_column(primary_key=True)
    choroba: Mapped[str] = mapped_column(nullable=True)

    objawy: Mapped[List['objawy']] = relationship(secondary="objawy_to_choroby")

Base.metadata.create_all(engine)

class Relate(DeclarativeBase):
    association_table = Table(
        "objawy_to_choroby",
        Base.metadata,
        Column("id_objawu", ForeignKey("objawy.id_objawy")),
        Column("id_choroby", ForeignKey("choroby.id_choroby")),
    )