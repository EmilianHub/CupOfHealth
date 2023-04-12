import datetime
from dataclasses import dataclass

from userJPA import User
from chorobyJPA import Diseases
from dbConnection import engine, Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey, DateTime


@dataclass
class UserDiseaseHistory(Base):
    __tablename__ = 'user_disease_history'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    user: Mapped[User] = relationship()
    user_symptoms: Mapped[bytes] = mapped_column(unique=False, nullable=False)
    disease_id: Mapped[int] = mapped_column(ForeignKey(Diseases.id_choroba))
    disease: Mapped[Diseases] = relationship()
    created: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), nullable=False, default=datetime.datetime.now())
    confidence: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"UserDiseaseHistory(id={self.id!r}, user={self.user!r}, userSymptoms={self.user_symptoms!r}, disease={self.disease!r})"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)
