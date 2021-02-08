import pyscreenshot as ImageGrab
import keyboard
import telepot

import os
import sys
import uuid
import time
import threading

import keyconfig as senv


SS_PATH = 'ss'
FILES_GRABBED = []


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


def upload_to_channel():
    while(True):
        if len(FILES_GRABBED):
            lock.acquire()
            file_path = FILES_GRABBED.pop(0)
            lock.release()
            try:
                bot = telepot.Bot(senv.TBOT_TOKEN)
                for CHAT_ID in senv.TBOT_CHAT_ID:
                    bot.sendDocument(CHAT_ID, document=open(file_path, 'rb'))
                print(f"{file_path} Uploaded to Channel")
                time.sleep(1) # cool down
            except Exception as e:
                print("Check Telegram Setup", str(e))


def main():
    print("Press Shift+F1 anytime to take a ss")
    print("Press Ctrl+C to quit")
    while (True):
        if keyboard.is_pressed("shift+F1"):
            file_path = grab_image()
            lock.acquire()
            FILES_GRABBED.append(file_path)
            lock.release()


if __name__ == "__main__":
    try:
        lock = threading.Lock()
        main_thread = threading.Thread(target=main, daemon=True)
        upload_thread = threading.Thread(target=upload_to_channel, daemon=True)
        main_thread.start()
        upload_thread.start()
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print("Exception Occured", str(e))
