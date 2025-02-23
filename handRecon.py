import cv2
import os
import time

import pyautogui
import pytweening
from cvzone.HandTrackingModule import HandDetector
from fontTools.merge.util import current_time

import interactiveInterface
import shared
import test


pyautogui.PAUSE = 0
#variables
parking = True
width, height = 640, 360
innerSensitivity = shared.sensitivity

gestureThreshold = 1100 #how high the line
last_index_finger_location = None
global_start_timer = None

sensitivity = 1
reset = 1



# pyautogui.PAUSE = 0





# camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4,height)


#hand Dector
detector = HandDetector(detectionCon=0.8, maxHands=1)


#Hand Mouse Variables
countAfterHolding = 0.0
countAfterHoldingStart = 0.0
startedCountingHold = False
countFromHolding = 0.0
countFromHoldingStart = 0.0
startedCountingFrom = False

from3 = False
touching = False
close = False
stuck = False
off = True
streak = False
theTime = 0.0



# frame_count = 0  # Initialize frame count
# frame_skip_rate = 2  # Process every 2nd frame (adjust this for balance)
delta_x = 0
delta_y = 0


COOLDOWN_TIME = 1.0
input_delay = 1.0
last_execution_time = 0
check_input = 0
gesture_timers = {}  # Track timers for each gesture

# def detect_gesture(gesture_active, method, input_delay, insert):
#     global g_start_timer
#
#     if gesture_active:
#
#         if g_start_timer is None:
#
#             g_start_timer = time.time()  # Start timer when gesture is first detected
#         else:
#             elapsed_time = time.time() - g_start_timer
#             if elapsed_time >= input_delay:
#                 print("Gesture recognized after holding" + insert)
#                 method()  # Trigger the method
#                 g_start_timer = None  # Reset timer after triggering
#
#     else:
#         g_start_timer = None  # Reset timer if gesture is not ac
current_gesture = None
previous_gesture = None
gesture_activated = {}







def detect_parking(gesture_active, method, input_delay, insert, gesture_id):
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



def detect_gesture_once(gesture_active, method, input_delay, insert, gesture_id, ):
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
            if fingers == [1, 1, 0, 0, 0]:
                print("click")
            else:
                interactiveInterface.park()
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




#hand detection Loop
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




        detect_parking(
            fingers == [0, 1, 0, 0, 1],
            interactiveInterface.park,
            0.1,
            "parking",
            "parking_gesture"  # Unique ID for
        )

        detect_parking(
            fingers == [1, 1, 0, 0, 1],
            interactiveInterface.drive,
            0.1,
            "drive",
            "drive_gesture"  # Unique ID for
        )

        # print(interactiveInterface.parker)

        if interactiveInterface.parker:  # not cy < gestureThreshold


            # Gesture 1: mouse pointer
            # Gesture 1: mouse pointer





            if fingers == [1, 1, 1, 0, 0] or fingers == [0, 0, 1, 1, 1] or fingers == [1, 0, 1, 1, 1]:


                if last_index_finger_location is not None:
                    test.move_dot(indexFinger[0], indexFinger[1], 20, "red")
                    # Calculate the change in position
                    delta_x = indexFinger[0] - last_index_finger_location[0]
                    delta_y = indexFinger[1] - last_index_finger_location[1]

                    # Move the mouse pointer
                if fingers == [1, 1, 1, 0, 0]:
                    innerSensitivity = 12


                if fingers == [0, 0, 1, 1, 1] or fingers == [1, 0, 1, 1, 1]:
                    innerSensitivity = 20

                interactiveInterface.move_mouse(delta_x , delta_y , innerSensitivity)
                last_index_finger_location = indexFinger


                # Update the previous index finger position

            else:
                # Reset the previous index finger position if the gesture is not active
                last_index_finger_location = None





            detect_gesture_once(
                fingers == [1, 1, 0, 0, 0],
                interactiveInterface.click,
                0.1,
                "click",
                "click_gesture"  # Unique ID for click
            )
            detect_gesture(
                fingers == [0, 0, 1, 0, 0],
                interactiveInterface.spam_click,
                0,
                "clickSpam",
                "clickSpam_gesture"  # Unique ID for click
            )

            # Gesture: back
            detect_gesture_once(
                fingers == [1, 0, 0, 0, 0],
                interactiveInterface.control_music_back,
                .5,
                "back",
                "back_gesture"  # Unique ID for pause
            )

            #go foward
            detect_gesture_once(
                fingers == [0, 1, 0, 0, 0],
                interactiveInterface.control_music_forward,
                .5,
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

            # pause
            detect_gesture(
                fingers == [0, 1, 1, 0, 0],
                interactiveInterface.scrollDown,
                0.0,
                "scrollDown",
                "scrollDown_gesture"  # Unique ID for pause
            )
            detect_gesture(
                fingers == [0, 1, 1, 0, 1],
                interactiveInterface.scrollUp,
                0.0,
                "scrollUp",
                "scrollUp_gesture"  # Unique ID for pause
            )




    key = cv2.waitKey(1)  # Capture keypress
    if key == ord('q'):
        break










