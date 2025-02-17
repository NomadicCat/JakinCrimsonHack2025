import cv2
import os
import time
import globals

import pyautogui
import pytweening
from cvzone.HandTrackingModule import HandDetector

import interactiveInterface



pyautogui.PAUSE = 0
#variables
width, height = 1280, 720
gestureThreshold = 1100 #how high the line
last_index_finger_location = None
global_start_timer = None
sensitivity = 1


globals.g_start_timer = None
mouse_control_active = False
globals.holding = 0.0
theTime = 0.0
globals.novelty = False

close = False
stuck = False
off = True
streak = False

countFromHolding = 0.0
countFromHoldingStart = 0.0
startedCountingFrom = False

from3 = False
touching = False

countAfterHolding = 0.0
countAfterHoldingStart = 0.0
startedCountingHold = False
# camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4,height)


#hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# frame_count = 0  # Initialize frame count
# frame_skip_rate = 2  # Process every 2nd frame (adjust this for balance)
delta_x = 0
delta_y = 0


COOLDOWN_TIME = 0.2

last_execution_time = 0
check_input = 0

g_start_timer = None



def detect_gesture(gesture_active, method, input_delay):
    """Detect a gesture with a hold duration based on the input_delay."""
    if gesture_active:
        if globals.g_start_timer is None:
            globals.g_start_timer = time.time()  # Start timer when gesture is first detected
        elif time.time() - globals.g_start_timer >= input_delay:
            if method == "mouse_control_active":
                globals.mouse_control_active = True  # Activate mouse movement
            else:
                method()  # Trigger the method
            globals.g_start_timer = None  # Reset timer after triggering
    else:
        globals.mouse_control_active = False  # Disable mouse movement when the gesture stops
        if not globals.novelty:
            globals.g_start_timer = None  # Reset timer if gesture is not active



while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (255, 0, 0), 5)
    hands, img = detector.findHands(img, flipType=False)
    cv2.imshow('Image', img)


    if hands:

        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx,cy = hand['center']
        lmList = hand['lmList']
        indexFinger = lmList[13][0], lmList[13][1]
        # Flip thumb detection manually for the correct hand
        if hand["type"] == "Right":
            fingers[0] = 1 - fingers[0]  # Invert thumb state for the right hand
            # print(fingers)
        if hand["type"] == "Left":
            fingers[0] = 1 - fingers[0]  # Invert thumb state for the right hand
            # print(fingers)

        # print(indexFinger)

        index_finger_tip = lmList[8][0:2]  # (x, y) of index fingertip
        thumb_tip = lmList[4][0:2]  # (x, y) of thumb tip

        distance, info, img = detector.findDistance(index_finger_tip, thumb_tip, img, color=(0, 255, 0), scale=10)

        index_finger_mcp = lmList[5][0:2]  # (x, y) of index fingertip
        index_finger_pip = lmList[6][0:2]  # (x, y) of thumb tip

        distance1, info2, img = detector.findDistance(index_finger_mcp, index_finger_pip, img, color=(0, 255, 0), scale=10)


        if True: #if hand is above line cy < gestureThreshold
            #Gesture 1: mouse pointer
            if fingers == [0,0,1,1,1] or fingers == [1,1,1,1,1] or fingers == [0,1,1,1,1] or fingers == [1,0,1,1,1]:
                if last_index_finger_location is not None:
                    # Calculate the change in position
                    delta_x = indexFinger[0] - last_index_finger_location[0]
                    delta_y = indexFinger[1] - last_index_finger_location[1]
                    # Move the mouse pointer

                    touching = distance < distance1

                    if touching and stuck: #Connected and Was Connect
                        close = True

                        from3 = False


                    elif touching and not stuck: #Connected and !Was Connected
                        close = True
                        stuck = True

                        countFromHoldingStart = time.time()

                        from3 = False


                    elif not touching and stuck: #!Connected and Was Connected

                        close = False
                        stuck = False

                        theTime = time.time() - countFromHoldingStart

                        countFromHolding = 0.0

                        from3 = True

                    elif not touching and not stuck: #!Connected and !Was Connected

                        close = False
                        from3 = False

                    if close:
                        interactiveInterface.move_mouse(delta_x * 3, delta_y * 3)
                        streak = True
                    else:
                        if theTime < COOLDOWN_TIME and from3:
                            print("theTime: ", theTime, "COOLDOWN_TIME: ", COOLDOWN_TIME)
                            interactiveInterface.click()
                            theTime = 0.0







                    # movement_threshold = 1  # Minimum change in pixels to move the mouse
                    # if abs(delta_x) > movement_threshold or abs(delta_y) > movement_threshold:
                    # Update the previous index finger position

                last_index_finger_location = indexFinger
            else:
                last_index_finger_location = None

            #gesture 2: press k
            # Gesture 2: Press K (hold gesture for input_delay seconds)
            if fingers == [1, 1, 0, 0, 1]:
                if globals.g_start_timer is None:
                    globals.g_start_timer = time.time()
                else:
                    elapsed_time = time.time() - globals.g_start_timer
                    #if elapsed_time >= input_delay:
                        #print("Gesture recognized after holding! Running interactiveInterface.pressk()...")
                        #interactiveInterface.pressk()
                        #gesture_start_time = None  # Reset after triggering
            else:
                gesture_start_time = None  # Reset if gesture is not active



            #gesture 3: click
            if fingers == [1,1,0,0,0]:
                gesture_active = fingers == [1, 1, 0, 0, 0]
                detect_gesture(gesture_active, interactiveInterface.click, 1.0)
                # current_time = 0
                # current_time = time.time()
                # if current_time - last_execution_time > COOLDOWN_TIME :
                #     print("Gesture recognized! Running interactiveInterface.click()...")
                #     interactiveInterface.click()  # Trigger your function
                #     last_execution_time = current_time  # Update the









    key = cv2.waitKey(1)  # Capture keypress
    if key == ord('q'):
        break










