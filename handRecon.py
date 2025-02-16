import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import interactiveInterface



#variables
width, height = 1280, 720
gestureThreshold = 500 #how high the line
playpause = [0,0,0,0,0]



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




        if cy < gestureThreshold : #if hand is above line

            # Gesture 1 - Left
            if fingers == [1, 0,0,0,0]:
                interactiveInterface.printHand()


            # Gesture 2 - right
            if fingers == [0, 0,0,0,1]:
                print("right")

            # Gesture 2 - right
            if fingers == [0, 1,1, 0, 0]:
                print("FUCK YOU TOO")



















    cv2.waitKey(1)
    key = cv2.waitKey(1)  # Capture keypress
    if key == ord('q'):
        break

