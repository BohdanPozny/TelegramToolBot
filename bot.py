from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.methods import DeleteWebhook
from config import TOKEN
import config
from handlers.control_pc import router as hcp_router
from handlers.commands import router as commands_router
import keyboard
from gi.repository import Notify

Notify.init("Telegram Bot Tool")
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    try:
        Notify.Notification.new(f"Start").show()

        dp.include_router(hcp_router)
        dp.include_router(commands_router)

        await bot(DeleteWebhook(drop_pending_updates=True))
        await dp.start_polling(bot)
    except Exception as e:
        Notify.Notification.new(f"Error {e}").show()
