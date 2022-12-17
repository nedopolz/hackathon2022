
class PortfolioRisk:
    @staticmethod
    def get_investment_horizon_index(investment_horizon: int) -> float:
        if investment_horizon < 1:
            return 0.3
        elif investment_horizon < 3:
            return 0.2
        elif investment_horizon < 5:
            return 0.15
        elif investment_horizon < 10:
            return 0.1
        return 0

    @staticmethod
    def get_obligations_index(obligations: bool) -> float:
        if obligations:
            return -0.2
        return 0.0

    @staticmethod
    def get_age_index(age: int) -> float:
        if age < 30:
            return 0.2
        elif age < 40:
            return 0.15
        elif age < 50:
            return 0.1
        return 0

    @staticmethod
    def get_goal_index(goal: str) -> float:
        if goal == "Медленное, но безопастное накопление":
            return 0.3
        elif goal == "Хочу копить, но приемлю определенные риски":
            return 0.4
        elif goal == "Максимальная доходность":
            return 0.5

    def calculate(self, answers: dict):
        investment_horizon = int(answers.get("investment_horizon"))
        age = int(answers.get("age"))
        goal = answers.get("goal")
        obligations = answers.get("obligations") == "True"
        risk_tolerance_index = 0
        risk_tolerance_index += self.get_investment_horizon_index(investment_horizon)
        risk_tolerance_index += self.get_obligations_index(obligations)
        risk_tolerance_index += self.get_age_index(age)
        risk_tolerance_index += self.get_goal_index(goal)
        return risk_tolerance_index


pr = PortfolioRisk()
print(pr.calculate({"investment_horizon": 1, "age": 38, "goal": "Медленное накопление", "obligations": False}))
