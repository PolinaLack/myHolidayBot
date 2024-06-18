import asyncio

from aiogram import Bot, Dispatcher
from aiohttp import ClientSession
from config import settings
from endpoints.handlers import router
from middleware.middleware import RepoMiddleware
from repository.holiday import HolidayRepo


async def main():
    async with ClientSession() as session:
        bot = Bot(
            token = settings.tg_bot_token,
        )

        dp = Dispatcher()
        
        holiday_repo = HolidayRepo(session=session)
        
        dp.message.middleware(RepoMiddleware(holiday_repo))
        
        dp.include_routers(router)

        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())