import numpy as np
import time
from pynput.keyboard import Controller


keyboard = Controller()


def find_pix(scr, x, y, key, color, color2, color3, color4, color5):
    col = scr[y][x]
    print(col, key)
    if np.array_equal(col[0: 3], np.array(color)) or np.array_equal(col[0: 3], np.array(color2)) or np.array_equal(col[0: 3], np.array(color3)) or np.array_equal(col[0: 3], np.array(color4)) or np.array_equal(col[0: 3], np.array(color5)):
        keyboard.press(key)
        print(1)
        time.sleep(0.01)
        keyboard.release(key)
