from pydantic import BaseModel


class InstrumentTypeSchema(BaseModel):
    name: str


class InstrumentTypeRiskDegree(InstrumentTypeSchema):
    instrument_type_risk_degree: float


class InstrumentSchema(BaseModel):
    id: int
    name: str
    amount: int
    price: float
    # type: InstrumentTypeSchema


class InstrumentRiskDegree(InstrumentSchema):
    degree: float
    type: InstrumentTypeRiskDegree


class PortfolioSchema(BaseModel):
    id: int
    name: str | None
    portfolio_risk_degree: float | None
    assets: list[InstrumentSchema]
    acceptable_risk_degree: float | None


class CreatePortfolio(BaseModel):
    name: str | None = None
    user_id: int
