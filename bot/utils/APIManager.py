import random

import aiohttp


class APIManager:
    def __init__(self):
        self.api_url = 'http://127.0.0.1:8021/'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    async def make_request(self, method, url, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, json=data, headers=self.headers) as response:
                s = await response.json(content_type=None)
                return s

    async def get_user_by_tg_id(self, tg_id):
        user = await self.make_request('GET', f'{self.api_url}user/{tg_id}')
        if not user:
            return None
        return user

    async def create_user(self, full_name, tg_id):
        await self.make_request('POST', f'{self.api_url}user/', data={"telegram_id": tg_id})
        return {"success": True}

    async def create_portfolio(self, tg_id):
        user = await self.get_user_by_tg_id(tg_id)
        if not user:
            return {"success": False, "message": "User not found"}
        portfolio = await self.make_request('POST', f'{self.api_url}portfolio/', data={"user_id": int(user['id'])})
        return portfolio

    async def get_questions(self):
        data = await self.make_request('GET', f'{self.api_url}questions/')
        return data

    async def save_answers(self, answers_list, portfolio_id):
        data = []
        portfolio_id = int(portfolio_id["id"])
        for answer in answers_list:
            data.append(
                {"portfolio_id": portfolio_id, "question_id": answer["question_id"], "answer_id": answer["answer_id"]})
        await self.make_request('POST', f'{self.api_url}questions/save', data=data)

    async def get_risk_profile(self, user_id):
        data = await self.make_request('GET', f'{self.api_url}user/{user_id}')
        if not data["risk_profile"]:
            return None
        risk_profile = float(data["risk_profile"])
        if risk_profile < 0.4:
            return "Самый низкий риск"
        if risk_profile < 0.6:
            return "Низкий риск"
        if risk_profile < 0.8:
            return "Средний риск"
        return "Высокий риск"

    async def get_portfolio(self, portfolio_id):
        return await self.make_request('GET', f'{self.api_url}portfolio/generate_portfolio/{portfolio_id}')
