from pynput.keyboard import Controller
import threading
from make_screenshot import make_screenshot
from find_PIX import find_pix


r = True
keyboard = Controller()
while r:
    scrn1 = make_screenshot({'top': 857, 'left': 820, 'height': 1, 'width': 286})
    s_thread = threading.Thread(target=find_pix, args=(scrn1, 0, 0, 's', [255, 247, 221], [255, 127, 0], [160, 80, 0], [208, 104, 0], [145, 136, 90]))
    d_thread = threading.Thread(target=find_pix, args=(scrn1, 137, 0, 'd', [255, 247, 221], [255, 127, 0], [160, 80, 0], [208, 104, 0], [145, 136, 90]))
    l_thread = threading.Thread(target=find_pix, args=(scrn1, 147, 0, 'l', [251, 221, 255], [101, 0, 255], [64, 0, 160], [83, 0, 208], [142, 90, 147]))
    m_thread = threading.Thread(target=find_pix, args=(scrn1, 285, 0, ';', [251, 221, 255], [101, 0, 255], [64, 0, 160], [83, 0, 208], [142, 90, 147]))
    s_thread.start()
    d_thread.start()
    l_thread.start()
    m_thread.start()
    s_thread.join()
    d_thread.join()
    l_thread.join()
    m_thread.join()
