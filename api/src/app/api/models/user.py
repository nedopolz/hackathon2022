from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Float
from sqlalchemy.orm import declarative_base, relationship

from sqlalchemy import MetaData

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_id = Column(Integer, nullable=True)
