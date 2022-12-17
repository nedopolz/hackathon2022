class InstrumentCalc:
    @staticmethod
    def get_investment_instrument(instrument: str) -> float:
        if instrument == "share":  # акция
            return 0.3
        elif instrument == "bond":   # облигация
            return 0.2

    @staticmethod
    def get_debt_div_eq(percent: str) -> float:
        percent = float(percent.replace('%', ''))
        if 0 < percent <= 20:
            return 0
        elif 20 < percent <= 40:
            return 0.1
        elif 40 < percent <= 60:
            return 0.2
        elif 60 < percent <= 90:
            return 0.3
        elif 90 < percent <= 100:
            return 0.4
        else:
            return 0.5

    @staticmethod
    def get_p_div_e(div: float) -> float:
        if div < 0:
            return 1
        elif 0 < div <= 5:
            return 0.1
        elif 5 < div <= 20:
            return 0.2
        elif 20 < div <= 40:
            return 0.3
        elif 40 < div <= 60:
            return 0.4
        elif 60 < div <= 80:
            return 0.5
        else:
            return 0.6

    @staticmethod
    def get_eps_percent(percent: str) -> float:
        percent = float(percent.replace('%', ''))
        if 20 < percent <= 30:
            return 0.1
        elif 30 < percent <= 50:
            return 0.2
        elif 50 < percent:
            return 0.3
        else:
            return 0

    @staticmethod
    def get_company_stonks_percent(percent: str) -> float:
        percent = float(percent.replace('%', ''))
        if 20 < percent <= 30:
            return 0.1
        elif 30 < percent <= 50:
            return 0.2
        elif 50 < percent:
            return 0.3
        else:
            return 0

    def instruments_risk_calculate(self, instrument_stats: dict):
        instrument = instrument_stats.get("type")
        risk_instrument_index = 0
        risk_instrument_index += self.get_investment_instrument(instrument)
        if instrument == "share":
            debt_div_eq = instrument_stats.get("de/eq")
            p_div_e = instrument_stats.get("p/e")
            eps_percent = instrument_stats.get("eps")
            company_stonks_percent = instrument_stats.get("stonks")
            risk_instrument_index += self.get_debt_div_eq(debt_div_eq)
            risk_instrument_index += self.get_p_div_e(p_div_e)
            risk_instrument_index += self.get_eps_percent(eps_percent)
            risk_instrument_index += self.get_company_stonks_percent(company_stonks_percent)
        return risk_instrument_index


ic = InstrumentCalc()
