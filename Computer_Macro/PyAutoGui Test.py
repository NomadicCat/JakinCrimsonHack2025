import pyautogui, win32gui, win32con, time, pygetwindow, pyperclip

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

