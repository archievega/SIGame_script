from keyboard import read_key
from pyscreenshot import grab
from pyautogui import click

print("Ready!")
while key:=read_key() not in ("p", "P", "з", "З"):
    try:
        if key in ("q", "Q", "й", "Й"):
            image = grab(childprocess=False)
            r, g, b = image.getpixel((380,670))
            if r == 255 and g == 255 and b == 255:
                click(x=1750, y=930)
    except Exception as e:
        print(f"Error: {e}")
    	continue
