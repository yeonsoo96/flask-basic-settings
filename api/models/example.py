from sqlalchemy import Column, UniqueConstraint, Integer, String

from manage import db


class Example(db.Model):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(name, age, name='uq_name_age'),
    )
