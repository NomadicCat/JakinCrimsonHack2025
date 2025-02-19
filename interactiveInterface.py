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

from subprocess import call

parker = True

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


# Install with: pip install playsound
from playsound3 import playsound

import wave
import numpy as np
import threading
import os
from tempfile import NamedTemporaryFile
from playsound3 import playsound
from tempfile import NamedTemporaryFile



def beep(freq, duration):

    def play_beep():
        volume = 0.1
        volume = max(0.0, min(volume, 1.0))

        sample_rate = 44100  # Sampling rate in Hz
        t = np.linspace(0, duration / 1000, int(sample_rate * duration / 1000), False)  # Time points
        note = np.sin(freq * t * 2 * np.pi)  # Sine wave for the desired frequency
        audio = (note * (2 ** 15 - 1) * volume).astype(np.int16) # Normalize audio
        audio = audio.astype(np.int16)  # Convert to 16-bit PCM format

        # Use a unique temporary file for each thread
        with NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            file_name = temp_file.name

        try:
            # Create the .wav file
            with wave.open(file_name, 'wb') as file:
                file.setnchannels(1)  # Mono audio
                file.setsampwidth(2)  # 2 bytes (16 bits per sample)
                file.setframerate(sample_rate)  # Sampling rate
                file.writeframes(audio.tobytes())  # Write the audio frames

            # Play the sound
            playsound(file_name)
        finally:
            # Always remove the file after playing
            if os.path.exists(file_name):
                os.remove(file_name)

    # Run the play_beep function in a separate thread
    beep_thread = threading.Thread(target=play_beep)
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
    drive()

def spam_click():
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()




def move_mouse(dx, dy): # Move the mouse by Δx and Δy
   # pyautogui.moveRel(dx, dy, duration=0.2)  # Move relative to the current position
   current_x, current_y = pyautogui.position()
   pyautogui.moveTo(current_x + dx,current_y + dy)

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
    beep(220, 50)
    parker = False

def drive():

    global parker
    beep(440, 50)
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