
class PortfolioRisk:
    @staticmethod
    def get_investment_horizon_index(investment_horizon: int) -> float:
        if investment_horizon == "менее года":
            return 0.3
        elif investment_horizon == "1-3 года":
            return 0.2
        elif investment_horizon == "3-5 лет":
            return 0.15
        elif investment_horizon == "5-10 лет":
            return 0.1
        return 0

    @staticmethod
    def get_obligations_index(obligations: str) -> float:
        if obligations == "да(":
            return -0.2
        return 0


    @staticmethod
    def get_age_index(age: int) -> float:
        if age == "18-30":
            return 0.2
        elif age == "31-40":
            return 0.15
        elif age == "41-50":
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
        investment_horizon = answers.get("На какой срок планируете инвестировать")
        age = answers.get("Укажите ваш возраст")
        goal = answers.get("Какие у вас цели инвестирования?")
        obligations = answers.get("Есть ли у вас семья, которую вы должны обеспечивать или какие-нибудь долговые обязательства(кредиты, ипотека и т.п.)?") == "True"
        risk_tolerance_index = 0
        risk_tolerance_index += self.get_investment_horizon_index(investment_horizon)
        risk_tolerance_index += self.get_obligations_index(obligations)
        risk_tolerance_index += self.get_age_index(age)
        risk_tolerance_index += self.get_goal_index(goal)
        return risk_tolerance_index


pr = PortfolioRisk()
