import tempfile

import pyautogui, time, pygetwindow as gw, pyperclip

import cv2
import os
import time
import keyboard
import playsound3
# import pyautogui
import pytweening
from cvzone.HandTrackingModule import HandDetector
from matplotlib.pyplot import eventplot
from pyautogui import leftClick
import wave
import numpy as np
import threading
import test

from subprocess import call

import kalmanfilter


parker = True


from playsound3 import playsound

import wave
import numpy as np
import threading
import os
from tempfile import NamedTemporaryFile
from playsound3 import playsound
from tempfile import NamedTemporaryFile



def beep(sound):
    def beeps():
        playsound(sound)

    # Run the play_beep function in a separate thread
    beep_thread = threading.Thread(target=beeps)
    beep_thread.start()






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


def click():
    pyautogui.click()
    drive()

def spam_click():
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()




def move_mouse(in_x, in_y, sens): # Move the mouse by Δx and Δy
   screen_width, screen_height = pyautogui.size()
   current_x, current_y = pyautogui.position()

   filtered_x, filtered_y = kalmanfilter.kalman_filter(current_x + in_x * sens, current_y + in_y * sens)

   safe_margin= 10
   new_x = max(safe_margin,min(screen_width - safe_margin - 1, filtered_x))
   new_y = max(safe_margin,min(screen_height - safe_margin - 1, filtered_y))


   # movement_threshold = 5
   # delta_x = abs(new_x - current_x)
   # delta_y = abs(new_y - current_y)
   #
   #
   # if delta_x > movement_threshold or delta_y > movement_threshold:
   pyautogui.moveTo(new_x, new_y)

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


# def control_music_back():
#     """Detects the focused application and controls music playback accordingly."""
#     active_app = get_active_window()
#
#     if active_app:
#         print(f"Active App: {active_app}")
#
#         # Check for Spotify
#         if "Spotify" in active_app or "spotify.exe" in active_app.lower():
#             if os.name == 'posix':  # macOS
#                 try:
#                     call(["osascript", "-e", 'tell application "Spotify" to previous track'])
#                 except Exception as e:
#                     print(f"Failed to control Spotify: {e}")
#             elif os.name == 'nt':  # Windows
#                 pyautogui.hotkey("media_prev_track")
#             else:
#                 print("Unsupported OS.")
#             print("Skipped to previous song on Spotify.")
#
#         # Check for YouTube in a browser
#         elif any(browser in active_app.lower() for browser in ["chrome", "firefox", "edge", "safari", "brave"]):
#             pyautogui.press('left')  # YouTube's seek backward shortcut
#             print("Rewound 5 seconds on YouTube.")
#
#         else:
#             print("No media application detected.")

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
                pyautogui.hotkey("media_next_track")
            else:
                print("Unsupported OS.")
            print("rewind to last song on Spotify.")

        # Check for YouTube in a browser
        elif any(browser in active_app.lower() for browser in ["chrome", "firefox", "edge", "safari", "brave", "opera"]):
            pyautogui.press('left')  # YouTube's seek backward shortcut
            print("left 5 seconds on YouTube.")

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

def park():
    global parker
    beep("sound/566887__lennartgreen__click-metronome-atonal-low.wav")
    parker = False

def drive():

    global parker
    beep("sound/29237__junggle__btn057.wav")
    parker = True

def scrollDown(steps=3, interval=0.01):
    """Scroll down smoothly with smaller steps."""
    if os.name == 'nt':  # Windows
        pyautogui.scroll(-20)
    else:
        for _ in range(steps):
            pyautogui.scroll(-1)  # Scroll down by one step
            time.sleep(interval)  # Wait briefly between steps


def scrollUp(steps=3, interval=0.01):
    if os.name == 'nt':  # Windows
        pyautogui.scroll(20)
    else:

        """Scroll up smoothly with smaller steps."""
        for _ in range(steps):
            pyautogui.scroll(1)  # Scroll up by one step
            time.sleep(interval)  # Wait briefly between steps



def test():
    if os.name == 'posix':  # macOS
        try:
            call(["osascript", "-e", 'tell application "Spotify" to playpause'])
        except Exception as e:
            print(f"Failed to control Spotify: {e}")