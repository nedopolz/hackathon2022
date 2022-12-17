import random


class PortfolioGeneration:
    def generate(self, personal_risk_index, instruments, investment_amount):
        users_instruments = []
        users_instruments_total_degree = 0
        totoal_amount = 0
        _limit = 5
        while totoal_amount < investment_amount:
            _limit += 1
            instrument = random.choice(instruments)
            instrument_risk_diff = abs(personal_risk_index - instrument["instrument_degree"])
            coeff = False
            if len(users_instruments) > 0:
                if (users_instruments_total_degree + instrument["instrument_degree"]) / len(users_instruments) <= 0.3:
                    coeff = True
            if instrument_risk_diff <= 0.3 or coeff:
                instrument_in = next(item for item in users_instruments if item["id"] == instrument["id"])
                if instrument_in:
                    instrument_in.update({instrument["id"]: instrument_in["amount"] + 1})
                else:
                    users_instruments.append({"amount": 1, "price": instrument["price"], "id": instrument["id"]})
                users_instruments_total_degree += instrument["instrument_degree"]
                totoal_amount += instrument["price"]
                _limit = 0

        return users_instruments


pg = PortfolioGeneration()
