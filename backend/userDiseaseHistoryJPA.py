from dbConnection import engine, Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class User(Base):
    __tablename__ = 'user_disease_history'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_symptoms: Mapped[str] = mapped_column()
    disease_id: Mapped[int] = mapped_column(ForeignKey("choroby.id_choroba"))
    disease: Mapped[""]


Base.metadata.create_all(engine)