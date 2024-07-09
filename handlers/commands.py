import os
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboard import main_menu
import aiogram

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привіт, {message.from_user.full_name}!", reply_markup=main_menu)

@router.message(Command("clear"))
async def clear(message: Message):
    await message.answer("Очистка", reply_markup=aiogram.types.ReplyKeyboardRemove())
