from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from models.holidays import Holiday
from repository.holiday import HolidayRepo

router = Router()

@router.message(Command("get_all"))
async def get_all(message: Message, repo: HolidayRepo):
    resp: list[Holiday] = await repo.get_all_holidays()
    
    resp_html = ""
    for holiday in resp: 
        resp_html += f"{holiday.user_name}: {holiday.start} - {holiday.end_date}\n"
    await message.answer(resp_html)


@router.message()
async def any_text(message: Message):
    await message.answer("Hello!")