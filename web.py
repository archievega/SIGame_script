from keyboard import read_key
from pyscreenshot import grab
from pyautogui import click

print("Ready!")
while key:=read_key() not in ("p", "P", "з", "З"):
    try:
        if key in ("q", "Q", "й", "Й"):
            image = grab(childprocess=False)
            r, g, b = image.getpixel((380,670))
            if r == 255 and g == 230 and b == 130:
                click(x=800, y=400, button='right')
    except Exception as e:
        print(f"Error: {e}")
    	continue
