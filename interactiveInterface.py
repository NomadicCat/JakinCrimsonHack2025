import pyautogui, time, pygetwindow as gw, pyperclip

import cv2
import os
import time

import pyautogui
import pytweening
from cvzone.HandTrackingModule import HandDetector
from pyautogui import leftClick
import globals

def get_active_window():
    # Get Active Window Title
    active_window = gw.getActiveWindow()
    if not active_window:
        return None

    # Simulate Ctrl + L (select address bar) and Ctrl + C (Copy URL)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5) # Waits for UT to respond
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Returns URL from Clipboard
    url = pyperclip.paste()
    return url

# print(get_active_window()) # Window URL for future reference

# Check Array and Activate Hotkey
def printHand():
    print("hello world")

def pressSpace():
    pyautogui.press('space', presses=1)

def pressk():
    pyautogui.press('k', presses=1)

def pressj():
    pyautogui.press('j', presses=1)

def pressl():
    pyautogui.press('l', presses=1)

def click():
    pyautogui.click()

def move_mouse(dx, dy):
    """Move the mouse based on dx, dy only if mouse_control_active is True."""
    if globals.mouse_control_active:
        pyautogui.moveRel(dx, dy)  # Move the mouse by relative delta values

def enable_mouse_control():
    globals.mouse_control_active = True
