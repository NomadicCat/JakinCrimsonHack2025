import cv2
import os
import time

import pyautogui
import pytweening
from cvzone.HandTrackingModule import HandDetector
from fontTools.merge.util import current_time

import interactiveInterface


pyautogui.PAUSE = 0
#variables
width, height = 1280, 720
gestureThreshold = 1100 #how high the line
last_index_finger_location = None
global_start_timer = None
g_start_timer = None
sensitivity = 1





# camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4,height)


#hand Dector
detector = HandDetector(detectionCon=0.8, maxHands=1)






# frame_count = 0  # Initialize frame count
# frame_skip_rate = 2  # Process every 2nd frame (adjust this for balance)
delta_x = 0
delta_y = 0


COOLDOWN_TIME = 1.0
last_execution_time = 0
check_input = 0


def detect_gesture(gesture_active, method, input_delay):
    global g_start_timer
    """
    Detect a gesture with a hold duration based on the input_delay.

    Args:
        gesture_active (bool): Whether the gesture is currently active.
        method (function): Function to execute when the gesture is held long enough.
        input_delay (float): Time in seconds to hold the gesture before triggering.
    """
    if gesture_active:
        if g_start_timer is None:
            g_start_timer = time.time()  # Start timer when gesture is first detected
        elif time.time() - g_start_timer >= input_delay:
            print("Gesture recognized after holding!")
            method()  # Trigger the method
            g_start_timer = None  # Reset timer after triggering
    else:
        g_start_timer = None  # Reset timer if gesture is not active


while True:

    # frame_count += 1
    # success, img = cap.read()
    # if frame_count % frame_skip_rate != 0:
    #     continue


        #import images


    #get camera and hand
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
        indexFinger = lmList[0][0], lmList[0][1]
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
            if fingers == [0,0,1,1,1] or fingers == [1,1,1,1,1]:
                if last_index_finger_location is not None:
                    # Calculate the change in position

                    delta_x = indexFinger[0] - last_index_finger_location[0]
                    delta_y = indexFinger[1] - last_index_finger_location[1]
                    # Move the mouse pointer
                    if fingers == [1,1,1,0,0]:
                        sensitivity = 0.5
                    if fingers == [0,0,0,0,0]:
                        sensitivity = 3






                interactiveInterface.move_mouse(delta_x * sensitivity ,delta_y * sensitivity)

                    # movement_threshold = 1  # Minimum change in pixels to move the mouse
                    # if abs(delta_x) > movement_threshold or abs(delta_y) > movement_threshold:
                    # Update the previous index finger position
                last_index_finger_location = indexFinger
            else:
                # Reset the previous index finger position if the gesture is not active
                last_index_finger_location = None

        #gesture 2: press k
            # Gesture 2: Press K (hold gesture for input_delay seconds)
            if fingers == [1, 1, 0, 0, 1]:
                if gesture_start_time is None:
                    gesture_start_time = time.time()  # Start the timer
                else:
                    elapsed_time = time.time() - gesture_start_time
                    if elapsed_time >= input_delay:
                        print("Gesture recognized after holding! Running interactiveInterface.pressk()...")
                        interactiveInterface.pressk()
                        gesture_start_time = None  # Reset after triggering
            else:
                gesture_start_time = None  # Reset if gesture is not active



            #gesture 3: click
            if fingers == [1,1,0,0,0]:
                detect_gesture(fingers == [1,1,0,0,0],interactiveInterface.click, 1.0)
                # current_time = 0
                # current_time = time.time()
                # if current_time - last_execution_time > COOLDOWN_TIME :
                #     print("Gesture recognized! Running interactiveInterface.click()...")
                #     interactiveInterface.click()  # Trigger your function
                #     last_execution_time = current_time  # Update the





        if distance1 < distance:
            print("CD: ", distance1)
        else:
            print("AB: ", distance)




    key = cv2.waitKey(1)  # Capture keypress
    if key == ord('q'):
        break










