from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Float
from sqlalchemy.orm import declarative_base, relationship

from sqlalchemy import MetaData

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, nullable=True)

    portfolio = relationship("Portfolio", back_populates="user")


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String)

    answer = relationship("Answer", back_populates="question")
    question_answer = relationship("QuestionsAnswer", back_populates="question")


class Answer(Base):
    __tablename__ = "answer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    answer = Column(String)
    question_id = Column(Integer, ForeignKey("question.id"), nullable=False)

    question = relationship("Question", back_populates="answer")
    question_answer = relationship("QuestionsAnswer", back_populates="answer")


class QuestionsAnswer(Base):
    __tablename__ = "questions_answer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("question.id"), nullable=False)
    answer_id = Column(Integer, ForeignKey("answer.id"), nullable=False)

    question = relationship("Question", back_populates="question_answer")
    answer = relationship("Answer", back_populates="question_answer")
    portfolio = relationship("Portfolio", back_populates="question_answer")


class Portfolio(Base):
    __tablename__ = "portfolio"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    questions_answer_id = Column(Integer, ForeignKey("questions_answer.id"), nullable=False)
    portfolio_risk_degree = Column(Float)
    acceptable_risk_degree = Column(Float)

    user = relationship("User", back_populates="portfolio")
    instrument_portfolio = relationship("InstrumentPortfolio", back_populates="portfolio")
    question_answer = relationship("QuestionsAnswer", back_populates="portfolio")


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
    instrument_degree = Column(Float)
    instrument_type_id = Column(Integer, ForeignKey("instrument_type.id"), nullable=False)
    amount = Column(Integer)
    price = Column(Float)

    instrument_portfolio = relationship("InstrumentPortfolio", back_populates="instrument")
    instrument_type = relationship("InstrumentType", back_populates="instrument")


class InstrumentPortfolio(Base):
    __tablename__ = "instrument_portfolio"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_id = Column(Integer, ForeignKey("instrument.id"), nullable=False)
    portfolio_id = Column(Integer, ForeignKey("portfolio.id"), nullable=False)

    instrument = relationship("Instrument", back_populates="instrument_portfolio")
    portfolio = relationship("Portfolio", back_populates="instrument_portfolio")
