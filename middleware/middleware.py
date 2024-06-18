from aiogram import BaseMiddleware
from aiogram.types import Message
from repository.holiday import HolidayRepo


class RepoMiddleware(BaseMiddleware):
    def __init__(self, repo: HolidayRepo):
        self.repo = repo

    async def __call__(self, handler, event: Message, data: dict):
        data['repo'] = self.repo
        await handler(event, data)
        