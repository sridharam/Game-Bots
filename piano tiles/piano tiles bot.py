import pyautogui
import time
import os
from PIL import ImageGrab, ImageOps
from numpy import *

 
pyautogui.click(341,210)
while True:
    box = (242, 477, 523,559)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    t = array(im.getcolors())
    t = t.sum()
    if  (t == 44084 or t == 26742):
        pyautogui.press("f")
        print("F")
    elif (t ==45745 or t == 32727):
        pyautogui.press("d")
        print("D")
    elif (t == 47745 or t== 35466):
        pyautogui.press("s")
        print("S")
    elif (t == 47410 or t == 35639):
        pyautogui.press("a")
        print("A")
