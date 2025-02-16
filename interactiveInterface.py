import pyautogui, time, pygetwindow as gw, pyperclip

import cv2
import os
import time
import keyboard

import pyautogui
import pytweening
from cvzone.HandTrackingModule import HandDetector
from matplotlib.pyplot import eventplot
from pyautogui import leftClick

from subprocess import call


# def get_active_window():
#     # Get Active Window Title
#     active_window = gw.getActiveWindow()
#     if not active_window:
#         return None
#
#     # Simulate Ctrl + L (select address bar) and Ctrl + C (Copy URL)
#     pyautogui.hotkey('ctrl', 'l')
#     time.sleep(0.5) # Waits for UT to respond
#     pyautogui.hotkey('ctrl', 'c')
#     time.sleep(0.5)
#
#     # Returns URL from Clipboard
#     url = pyperclip.paste()
#     return url

# print(get_active_window()) # Window URL for future reference

# Check Array and Activate Hotkey
def get_active_window():
    """Returns the name of the currently focused application."""
    if os.name == "posix":  # macOS / Linux
        try:
            from AppKit import NSWorkspace
            return NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
        except ImportError:
            print("AppKit is required for macOS but not installed.")
            return None
    elif os.name == "nt":  # Windows
        try:
            import win32gui
            import win32process
            import psutil

            hwnd = win32gui.GetForegroundWindow()
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            for proc in psutil.process_iter(attrs=["pid", "name"]):
                if proc.info["pid"] == pid:
                    return proc.info["name"]
        except ImportError:
            print("pywin32 is required for Windows but not installed.")
            return None
    return None

def printHand():
    print("hello world")

# def pressSpace():
#     pyautogui.press('space', presses=1)
#
# def pressk():
#     pyautogui.press('k', presses=1)
#
# def pressj():
#     pyautogui.press('j', presses=1)
#
# def pressl():
#     pyautogui.press('l', presses=1)

def click():
    pyautogui.click()

def move_mouse(dx, dy): # Move the mouse by Δx and Δy
   # pyautogui.moveRel(dx, dy, duration=0.2)  # Move relative to the current position
   pyautogui.moveRel(dx, dy)

def skip_right():

    pyautogui.press('right')

def skip_left():
    pyautogui.press('left')



def pause():
    if os.name == 'posix':  # macOS
        try:
            # Directly tell Spotify to play/pause
            call(["osascript", "-e", 'tell application "Spotify" to playpause'])

        except Exception as e:
            print(f"Failed to control Spotify: {e}")
    elif os.name == 'nt':  # Windows
        pyautogui.hotkey("playpause")
    else:
        print("Unsupported OS.")


def control_music_back():
    """Detects the focused application and controls music playback accordingly."""
    active_app = get_active_window()

    if active_app:
        print(f"Active App: {active_app}")

        # Check for Spotify
        if "Spotify" in active_app or "spotify.exe" in active_app.lower():
            if os.name == 'posix':  # macOS
                try:
                    call(["osascript", "-e", 'tell application "Spotify" to previous track'])
                except Exception as e:
                    print(f"Failed to control Spotify: {e}")
            elif os.name == 'nt':  # Windows
                pyautogui.hotkey("media_prev_track")
            else:
                print("Unsupported OS.")
            print("Skipped to previous song on Spotify.")

        # Check for YouTube in a browser
        elif any(browser in active_app.lower() for browser in ["chrome", "firefox", "edge", "safari", "brave"]):
            pyautogui.press('left')  # YouTube's seek backward shortcut
            print("Rewound 5 seconds on YouTube.")

        else:
            print("No media application detected.")

def control_music_forward():
    """Detects the focused application and controls music playback accordingly."""
    active_app = get_active_window()

    if active_app:
        print(f"Active App: {active_app}")

        # Check for Spotify
        if "Spotify" in active_app or "spotify.exe" in active_app.lower():
            if os.name == 'posix':  # macOS
                try:
                    call(["osascript", "-e", 'tell application "Spotify" to next track'])
                except Exception as e:
                    print(f"Failed to control Spotify: {e}")
            elif os.name == 'nt':  # Windows
                pyautogui.hotkey("media_next_track")
            else:
                print("Unsupported OS.")
            print("Skipped to next song on Spotify.")

        # Check for YouTube in a browser
        elif any(browser in active_app.lower() for browser in ["chrome", "firefox", "edge", "safari", "brave", "opera"]):
            pyautogui.press('right')  # YouTube's seek backward shortcut
            print("forward 5 seconds on YouTube.")

        else:
            print("No media application detected.")
def control_music_pause():
    """Detects the focused application and controls music playback accordingly."""
    active_app = get_active_window()

    if active_app:
        print(f"Active App: {active_app}")

        # Check for Spotify
        if "Spotify" in active_app or "spotify.exe" in active_app.lower():
            if os.name == 'posix':  # macOS
                try:
                    call(["osascript", "-e", 'tell application "Spotify" to playpause'])
                except Exception as e:
                    print(f"Failed to control Spotify: {e}")
            elif os.name == 'nt':  # Windows
                pyautogui.hotkey("playpause")
            else:
                print("Unsupported OS.")
            print("paused on Spotify.")

        # Check for YouTube in a browser
        elif any(browser in active_app.lower() for browser in ["chrome", "firefox", "edge", "safari", "brave", "opera"]):
            pyautogui.press('space')  # YouTube's seek backward shortcut
            print("pause on YouTube.")

        else:
            print("No media application detected.")

