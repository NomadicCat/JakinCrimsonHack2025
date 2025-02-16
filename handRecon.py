import cv2
import os
import time

from shared import get_sensitivity
import pyautogui
import pytweening
from cvzone.HandTrackingModule import HandDetector
from fontTools.merge.util import current_time

import interactiveInterface




class HandReconExit(Exception):  # Custom exception
    pass


pyautogui.PAUSE = 0
#variables
width, height = 1280, 720
gestureThreshold = 1100 #how high the line
last_index_finger_location = None
global_start_timer = None

sensitivity = 1
reset = 1





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
input_delay = 1.0
last_execution_time = 0
check_input = 0
gesture_timers = {}  # Track timers for each gesture


current_gesture = None
previous_gesture = None
gesture_activated = {}
indexFinger = None

def detect_gesture_once(gesture_active, method, input_delay, insert, gesture_id):
    global gesture_timers
    global current_gesture, previous_gesture



    if gesture_active:

        if current_gesture != gesture_id:
            # Reset the timer for this gesture
            gesture_timers[gesture_id] = None
            gesture_activated[gesture_id] = False
            current_gesture = gesture_id  # Update current gesture

        if gesture_id not in gesture_timers:
            gesture_timers[gesture_id] = None

        if gesture_timers[gesture_id] is None:
            gesture_timers[gesture_id] = time.time()  # Start timer

        elapsed_time = time.time() - gesture_timers[gesture_id]
        if elapsed_time >= input_delay and not gesture_activated[gesture_id]:
            print(f"Gesture recognized after holding {insert}")
            method()
            # gesture_timers[gesture_id] = None  # Reset timer
            gesture_activated[gesture_id] = True
    else:
        # Reset timer and activation state if gesture is not active
        if gesture_id in gesture_timers:
            gesture_timers[gesture_id] = None
            gesture_activated[gesture_id] = False

        # Update previous gesture when the gesture is no longer active
        if current_gesture == gesture_id:
            previous_gesture = current_gesture
            current_gesture = None


def detect_gesture(gesture_active, method, input_delay, insert, gesture_id):


    if gesture_active:

        if gesture_id not in gesture_timers:
            gesture_timers[gesture_id] = None

        if gesture_timers[gesture_id] is None:
            gesture_timers[gesture_id] = time.time()  # Start timer
        else:
            elapsed_time = time.time() - gesture_timers[gesture_id]
            if elapsed_time >= input_delay:
                print(f"Gesture recognized after holding {insert}")
                method()
                gesture_timers[gesture_id] = None  # Reset timer
    else:
        # Reset timer if gesture is not active
        if gesture_id in gesture_timers:
            gesture_timers[gesture_id] = None

parking = True
fingers = [0, 0, 0, 0, 0]


while True:


    # frame_count += 1
    # success, img = cap.read()
    # if frame_count % frame_skip_rate != 0:
    #     continue


        #import images


    #get camera and hand
    success, img = cap.read()
    if not success:
        print("ee")
        continue  # Skip iteration if camera frame is not successfully captured

    img = cv2.flip(img, 1)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (255, 0, 0), 5)
    hands, img = detector.findHands(img, flipType=False)
    cv2.imshow('Image', img)


    # cy = gestureThreshold + 1


    while True:
        sensitivity = get_sensitivity()

        if interactiveInterface.parker:  # if hand is above line cy < gestureThreshold

            # Gesture 1: mouse pointer
            if fingers == [1, 1, 1, 0, 0] or fingers == [0, 0, 0, 0, 0]:
                if last_index_finger_location is not None:
                    # Calculate the change in position

                    delta_x = indexFinger[0] - last_index_finger_location[0]
                    delta_y = indexFinger[1] - last_index_finger_location[1]
                    # Move the mouse pointer
                    if fingers == [1, 1, 1, 0, 0]:
                        sensitivity = 0.5
                    if fingers == [0, 0, 0, 0, 0]:
                        sensitivity = 3

                    interactiveInterface.move_mouse(delta_x * sensitivity ,delta_y * sensitivity)

                interactiveInterface.move_mouse(delta_x * sensitivity, delta_y * sensitivity)

                # movement_threshold = 1  # Minimum change in pixels to move the mouse
                    # if abs(delta_x) > movement_threshold or abs(delta_y) > movement_threshold:
                    # Update the previous index finger position
                last_index_finger_location = indexFinger
            else:
                # Reset the previous index finger position if the gesture is not active
                last_index_finger_location = None

        #gesture 2: press k
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



            detect_gesture(
                fingers == [1, 1, 0, 0, 0],
                interactiveInterface.click,
                1.0,
                "click",
                "click_gesture"  # Unique ID for click
            )

            # Gesture: back
            detect_gesture_once(
                fingers == [1, 0, 0, 0, 0],
                interactiveInterface.control_music_back,
                0.2,
                "back",
                "back_gesture"  # Unique ID for pause
            )

            #go foward
            detect_gesture_once(
                fingers == [0, 1, 0, 0, 0],
                interactiveInterface.control_music_forward,
                0.2,
                "forward",
                "forward_gesture"  # Unique ID for pause
            )
            #pause
            detect_gesture_once(
                fingers == [1, 0, 0, 0, 1],
                interactiveInterface.control_music_pause,
                0.2,
                "pause",
                "pause_gesture"  # Unique ID for pause
            )



    key = cv2.waitKey(1)  # Capture keypress
    if key == ord('q'):
        break










