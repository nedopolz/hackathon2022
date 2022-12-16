import random


class APIManager:
    def __init__(self):
        self.api_key = ''
        self.api_secret = ''

    async def get_user_by_tg_id(self, tg_id):
        return {"id": "1", "name": "User 1"}

    async def create_user(self, full_name, tg_id):
        return {"success": True}

    async def get_question(self, user_id):
        data = [
            {"id": "1", "name": "Question 1",
             "answers": [{"id": 1, "text": "Answer 1"}, {"id": 2, "text": "Answer 2"}, {"id": 3, "text": "Answer 3"}]},
            {"id": "2", "name": "Question 2",
             "answers": [{"id": 1, "text": "Answer 1"}, {"id": 2, "text": "Answer 2"}, {"id": 3, "text": "Answer 3"}]},
            {"id": "3", "name": "Question 3",
             "answers": [{"id": 1, "text": "Answer 1"}, {"id": 2, "text": "Answer 2"}, {"id": 3, "text": "Answer 3"}]},
            {"id": "4", "name": "Question 4",
             "answers": [{"id": 1, "text": "Answer 1"}, {"id": 2, "text": "Answer 2"}, {"id": 3, "text": "Answer 3"}]},
            {"id": "5", "name": "Question 5",
             "answers": [{"id": 1, "text": "Answer 1"}, {"id": 2, "text": "Answer 2"}, {"id": 3, "text": "Answer 3"}]},
            {}
        ]
        return random.choice(data)

    async def save_answer(self, answer_id, question_id, user_id):
        return {"success": True}

    async def get_risk_profile(self, user_id):
        data = [
            {"id": "1", "name": "Низкая толерантность к риску"},
            {"id": "2", "name": "Умеренная толерантность к риску"},
            {"id": "3", "name": "Высокая толерантность к риску"},
        ]
        return random.choice(data)

    async def get_portfolio(self, user_id):
        return {"id": "1", "name": "Portfolio 1", "risk_profile": "1",
                "assets": [{"id": "1", "name": "apple", "amount": "10", "total_price": "200"},
                           {"id": "2", "name": "google", "amount": "10", "total_price": "200"},
                           {"id": "3", "name": "Газпром", "amount": "10", "total_price": "200"}]}
