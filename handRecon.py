import cv2
import os
from cvzone.HandTrackingModule import HandDetector
#variables
width, height = 1280, 720



# camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4,height)


#hand Dector
detector = HandDetector(detectionCon=0.8, maxHands=1)







while True:

    #import images


    #get camera and hand
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    cv2.imshow('Image', img)



    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        # Flip thumb detection manually for the correct hand
        if hand["type"] == "Right":
            fingers[0] = 1 - fingers[0]  # Invert thumb state for the right hand
        print(fingers)

        



    cv2.waitKey(1)
    key = cv2.waitKey(1)  # Capture keypress
    if key == ord('q'):
        break

