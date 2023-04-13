from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from chorobyJPA import Diseases
from dbConnection import engine, Base


class Localization(Base):
    __tablename__ = 'localization'

    id_loc: Mapped[int] = mapped_column(primary_key=True)
    woj: Mapped[str] = mapped_column(nullable=True)
    miasto: Mapped[str] = mapped_column(nullable=True)
    choroba_id: Mapped[int] = mapped_column(ForeignKey(Diseases.id_choroba))
    choroba: Mapped[Diseases] = relationship()
    created: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False, default=datetime.now())


Base.metadata.create_all(engine)
