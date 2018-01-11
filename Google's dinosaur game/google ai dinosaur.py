import pyautogui
import time
import os
from PIL import ImageGrab, ImageOps
from numpy import *

    
def main():
    pyautogui.click(x = 341, y = 410)
    pyautogui.moveTo(341,210)
    while True:
        box = (220, 400, 258 , 446)
        im = ImageOps.grayscale(ImageGrab.grab(box))
        t = array(im.getcolors())
        t = t.sum()
        print(t)
        if not t == 1995:
            pyautogui.press("space")

main()
 
