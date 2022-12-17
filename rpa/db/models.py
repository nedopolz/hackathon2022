from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Float
from sqlalchemy.orm import declarative_base, relationship

from sqlalchemy import MetaData

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class InstrumentType(Base):
    __tablename__ = "instrument_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    instrument_type_risk_degree = Column(Float)

    instrument = relationship("Instrument", back_populates="instrument_type")


class Instrument(Base):
    __tablename__ = "instrument"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    instrument_type_degree = Column(Float)
    instrument_type_id = Column(Integer, ForeignKey("instrument_type.id"), nullable=False)

    instrument_portfolio = relationship("InstrumentPortfolio", back_populates="instrument")
    instrument_type = relationship("InstrumentType", back_populates="instrument")

