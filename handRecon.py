import cv2

#variables
width, height = 1280, 720



# camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4,height)

while True:
    success, img = cap.read()
    cv2.imshow('Image', img)
    cv2.waitKey(1)
    key = cv2.waitKey(1)  # Capture keypress
    if key == ord('q'):
        break