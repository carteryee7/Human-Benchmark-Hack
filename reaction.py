from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# X: 1951 Y:  594 RGB: ( 43, 135, 209)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(1951, 594)[0] == 75:
        click(1170, 785)
    

