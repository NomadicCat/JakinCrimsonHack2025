# gesture 2: press k
# Gesture 2: Press K (hold gesture for input_delay seconds)
# if fingers == [1, 1, 0, 0, 1]:
#     gesture_start_time = None
#     if gesture_start_time is None:
#         gesture_start_time = time.time()  # Start the timer
#     else:
#         elapsed_time = time.time() - gesture_start_time
#         if elapsed_time >= input_delay:
#             print("Gesture recognized after holding! Running interactiveInterface.pressk()...")
#             interactiveInterface.pressk()
#             gesture_start_time = None  # Reset after triggering
# else:
#     gesture_start_time = None  # Reset if gesture is not active

# Gesture: Click (fingers == [1,1,0,0,0])




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


index_finger_tip = lmList[8][0:2]  # (x, y) of index fingertip
thumb_tip = lmList[4][0:2]  # (x, y) of thumb tip

distance, info, img = detector.findDistance(index_finger_tip, thumb_tip, img, color=(0, 255, 0),
                                            scale=10)

index_finger_mcp = lmList[5][0:2]  # (x, y) of index fingertip
index_finger_pip = lmList[6][0:2]  # (x, y) of thumb tip

distance1, info2, img = detector.findDistance(index_finger_mcp, index_finger_pip, img,
                                              color=(0, 255, 0), scale=10)

if last_index_finger_location is not None:
    # Calculate the change in position
    delta_x = indexFinger[0] - last_index_finger_location[0]
    delta_y = indexFinger[1] - last_index_finger_location[1]
    # Move the mouse pointer

    touching = distance < distance1

    if touching and stuck:  # Connected and Was Connect
        close = True

        from3 = False


    elif touching and not stuck:  # Connected and !Was Connected
        close = True
        stuck = True

        countFromHoldingStart = time.time()

        from3 = False


    elif not touching and stuck:  # !Connected and Was Connected

        close = False
        stuck = False

        theTime = time.time() - countFromHoldingStart

        countFromHolding = 0.0

        from3 = True

    elif not touching and not stuck:  # !Connected and !Was Connected

        close = False
        from3 = False

    if close:
        a = shared.sensitivity * 2
        interactiveInterface.move_mouse(delta_x * a, delta_y * a)
        streak = True
    else:
        if theTime < COOLDOWN_TIME and from3:
            print("Clicked")
            interactiveInterface.click()
            theTime = 0.0


