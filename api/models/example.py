from sqlalchemy import Column, UniqueConstraint, Integer, String, Unicode

from db import Base


class Example(Base):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode, nullable=False)
    age = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(name, age, name='uq_name_age'),
    )
