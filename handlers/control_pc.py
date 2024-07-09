from aiogram.types import Message, FSInputFile, InputFile
from keyboard import control_pc_menu
from gi.repository import Notify
from aiogram import F, Router
from datetime import datetime
from pdb import run
import asyncio
import config
from cv2 import VideoCapture, imwrite
import os

async def photo(folder: str, command: str, message: Message):
    file_name = f"{config.abs_path}/{folder}/{message.from_user.username}__{str(datetime.now()).replace(' ', '_')}.png"
    os.system(f"{command} {file_name}")

    await message.answer(f"Screenshot")
    file = FSInputFile(file_name)
    await message.answer_photo(file)

router = Router()

@router.message(F.text == "Notify")
async def notify(message: Message):
    Notify.Notification.new(f"Notify {message.from_user.full_name} {message.from_user.username}\n\n {message.text}").show()

@router.message(F.text == config.message_command["ControlPC"])
async def control_pc(message: Message):
    await message.answer("ControlPC", reply_markup=control_pc_menu)

@router.message(F.text == config.message_command["PowerOff"])
async def power_off(message: Message):
    print(message.from_user.username in config.ADMIN_USERNAME, '\n\n', message.from_user.username, '\n\n')
    if message.from_user.username in config.ADMIN_USERNAME:
        await message.answer("PowerOff")
        asyncio.run(os.system("poweroff"))
    elif message.from_user.username == config.DIMA:
        await message.answer(f"Хуй тобі {message.from_user.full_name}!")
    else:
        print(message.from_user.id, '\n\n')
        await message.answer("Доступ заборонено\n\nВаш ID: " + str(message.from_user.id))

@router.message(F.text == config.message_command["Reboot"])
async def reboot(message: Message):
    print(message.from_user.username in config.ADMIN_USERNAME, '\n\n', message.from_user.username, '\n\n')

    if message.from_user.username in config.ADMIN_USERNAME:
        await message.answer("Reboot")
        asyncio.run(os.system("reboot"))
    elif message.from_user.username == config.DIMA:
        await message.answer(f"Хуй тобі {message.from_user.full_name}!")
    else:
        print(message.from_user.id, '\n\n')
        await message.answer("Доступ заборонено\n\nВаш ID: " + str(message.from_user.id))

@router.message(F.text == config.message_command["Screenshot"])
async def screenshot(message: Message):
    Notify.Notification.new(f"Screenshot {message.from_user.full_name} {message.from_user.username}").show()
    # os.system(f"gnome-screenshot screenshot.png")

    await photo("Screenshots", "import -window root", message)

    # file_name = f"{config.abs_path}/{'Screenshots'}/{message.from_user.username}__{str(datetime.now()).replace(' ', '_')}.png"
    # os.system(f"import -window root {file_name}")


    # await message.answer(f"Screenshot")
    # file = FSInputFile(file_name)
    # await message.answer_photo(file)

@router.message(F.text == config.message_command['TakePicture'])
async def take_picture(message: Message):
    Notify.Notification.new(f"TakePicture {message.from_user.full_name} {message.from_user.full_name}").show()

    await photo("Pictures", "streamer -f jpeg -o", message)

    # file_name = f"{config.abs_path}/{'Pictures'}/{message.from_user.username}__{str(datetime.now()).replace(' ', '_')}.jpeg"
    # os.system(f"streamer -f jpeg -o {file_name}")


    # await message.answer(f"TakePicture")
    # file = FSInputFile(file_name)
    # await message.answer_photo(file)


