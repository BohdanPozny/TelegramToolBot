from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import message_command

main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=message_command["ControlPC"])],
    ],
    resize_keyboard=True)

control_pc_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=message_command["PowerOff"]), KeyboardButton(text=message_command["Reboot"]),],
    [KeyboardButton(text=message_command["Screenshot"]), KeyboardButton(text=message_command["TakePicture"]),],
    ],
    resize_keyboard=True)
