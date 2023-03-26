from sqlalchemy import ForeignKey

from userJPA import User
from chorobyJPA import Diseases
from dbConnection import engine, Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship



class Loca(Base):
    __tablename__ = 'localization'

    id_loc: Mapped[int] = mapped_column(primary_key=True)
    woj: Mapped[str] = mapped_column(nullable=True)
    miasto: Mapped[str] = mapped_column(nullable=True)
    choroba_id: Mapped[int] = mapped_column(ForeignKey(Diseases.id_choroba))
    choroba: Mapped[Diseases] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id),nullable=True)
    user: Mapped[User] = relationship()

Base.metadata.create_all(engine)
