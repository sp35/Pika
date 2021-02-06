import pyscreenshot as ImageGrab
import keyboard
import telepot

import os
import sys
import uuid

import keyconfig as senv


SS_PATH = 'ss'


def gen_file_name():
    return "pic_%s.png" % str(uuid.uuid4())


def grab_image():
    if not os.path.exists(SS_PATH):
        os.makedirs('ss')
    file_path = os.path.join(SS_PATH, gen_file_name())
    
    im = ImageGrab.grab()
    im.save(file_path)
    print(f"Image saved at {file_path}")

    return file_path


def upload_to_channel(file_path):
    try:
        bot = telepot.Bot(senv.TBOT_TOKEN)
        for CHAT_ID in senv.TBOT_CHAT_ID:
            bot.sendPhoto(CHAT_ID, photo=open(file_path, 'rb'))
        print("File Uploaded to Channel")
    except Exception as e:
        print("Check Telegram Setup", str(e))


def main():
    print("Press Shift+F1 anytime to take a ss")
    print("Press Ctrl+C to quit")
    while (True):
        if keyboard.is_pressed("shift+F1"):
            file_path = grab_image()
            upload_to_channel(file_path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print("Exception Occured", str(e))
