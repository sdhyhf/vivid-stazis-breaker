from mss import mss
import numpy as np


def make_screenshot(mon):
    with mss() as sct:
        img = sct.grab(mon)
        return np.array(img)
