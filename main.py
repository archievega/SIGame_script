# -*- coding: utf-8 -*-q
import keyboard
from PIL import ImageChops
from pyscreenshot import grab
import pyautogui

while True:
    try:
        if keyboard.read_key() == "q":
            im = grab(childprocess=False)
            r, g, b = im.getpixel((370, 7))
            if r == 255 and g == 230 and b == 130:
                pyautogui.click(x=1730, y=930)
            pass
    except:
        pass
