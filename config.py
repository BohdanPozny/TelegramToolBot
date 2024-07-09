from decouple import config 
import os
import emoji
emoji.EMOJI_UNICODE = True

TOKEN = config("BOT_TOKEN")
ADMIN_USERNAME = config("ADMIN_USERNAME", None)
DIMA= config("DIMA", None)
abs_path = os.path.abspath(__file__).replace("/config.py", "")

message_command = {
    "PowerOff": f"PowerOff{emoji.emojize(':no_entry:')}",
    "Reboot": f"Reboot{emoji.emojize(':repeat_button:')}",
    "Screenshot": f"Screenshot{emoji.emojize(':camera:')}",
    "ControlPC": f"ControlPC{emoji.emojize(':keyboard:')}",
    "TakePicture": f"TakePicture{emoji.emojize(':camera_with_flash:')}"
}

print(type(ADMIN_USERNAME))

print(TOKEN, ADMIN_USERNAME, "\n\n\n")
