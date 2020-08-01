# em1tao
# import modules
import keyboard
from pyscreenshot import grab
import pyautogui

# wait for press key
while True:
    try:
        if keyboard.read_key() == "q":
            im = grab(childprocess=False)
            r, g, b = im.getpixel((370, 7))
            if r == 255 and g == 230 and b == 130:
                pyautogui.click(x=1730, y=930)
            pass
        if keyboard.read_key() == "p":
            break
    except:
    	continue
