import cv2
import os
import time

import pyautogui
import pytweening
from cvzone.HandTrackingModule import HandDetector
import interactiveInterface


pyautogui.PAUSE = 0
#variables
width, height = 1280, 720
gestureThreshold = 500 #how high the line
last_index_finger_location = None




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
        indexFinger = lmList[8][0], lmList[8][1]
        # Flip thumb detection manually for the correct hand
        if hand["type"] == "Right":
            fingers[0] = 1 - fingers[0]  # Invert thumb state for the right hand
            # print(fingers)
        if hand["type"] == "Left":
            fingers[0] = 1 - fingers[0]  # Invert thumb state for the right hand
            # print(fingers)

        # print(indexFinger)



        if cy < gestureThreshold : #if hand is above line

            #Gesture 1: mouse pointer
            if fingers == [0,1,1,0,0]:
                if last_index_finger_location is not None:
                    # Calculate the change in position

                    delta_x = indexFinger[0] - last_index_finger_location[0]
                    delta_y = indexFinger[1] - last_index_finger_location[1]
                    # Move the mouse pointer
                    interactiveInterface.move_mouse(delta_x,delta_y)

                    # movement_threshold = 1  # Minimum change in pixels to move the mouse
                    # if abs(delta_x) > movement_threshold or abs(delta_y) > movement_threshold:
                    # Update the previous index finger position
                last_index_finger_location = indexFinger
            else:
                # Reset the previous index finger position if the gesture is not active
                last_index_finger_location = None







            # Gesture
            # if fingers == [1, 0,0,0,0]:
            #     print("left")


    cv2.waitKey(1)
    key = cv2.waitKey(1)  # Capture keypress
    if key == ord('q'):
        break

