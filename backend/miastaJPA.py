from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from dbConnection import engine, Base
from wojeJPA import Woje

class Miasta(Base):
    __tablename__ = 'miasta'

    id: Mapped[int] = mapped_column(primary_key=True)
    woj_id: Mapped[int] = mapped_column(ForeignKey(Woje.id))
    woje: Mapped[List[Woje]] = relationship()
    nazwa: Mapped[str] = mapped_column()


Base.metadata.create_all(engine)
