import pyautogui, time, pygetwindow as gw, pyperclip


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

print(get_active_window()) # Window URL for future reference

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

def move_mouse(dx, dy): # Move the mouse by Δx and Δy
   pyautogui.moveRel(dx, dy, duration=0.2)  # Move relative to the current position
   time.sleep(0.3)