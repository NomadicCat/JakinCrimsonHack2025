# JakinCrimsonHack2025
!! Reccomended to pull from Dist_Build or hand_with_ui for functional build !!
Hand gesture computer controller

From thumb to pinky the array of fingers are 0 for closed 1 for open



Set up
Python 3.12.0
import cvzone, pile

This project utilizes the MediaPipe Hand Landmark model to be able to recognize different hand signs with the webcamera.

Hand signs and their meanings:

[0,1,0,0,1] - lock hand recognition
[1,1,0,0,1] - Unlock hand recognition(can do gestures)

BASIC MOUSE MOVEMENT

[0,0,0,0,0] - grab mouse
[1,1,1,0,0] - slow drag
[1,1,0,0,0] - click
[0,1,1,0,0] - scroll down
[0,1,1,0,1] - scroll up
[1,0,0,0,0] - go back
[0,1,0,0,0] - go foward
[1,0,0,0,1] - pause




- Index + middle finger + thumb outstretched: Moves cursor in slower speed for precision clicking. 
- Flipping down middle finger initiates a click.
- Fist: drags mouse at faster speed. 

SPOTIFY PLAYBACK
- Fist with outstretched thumb: Skip backwards a song/rewind.
- Fist with outstretched index finger: Skip forwards a song.

HAND RECOGNITION TOGGLING
- "Rock and Roll" Hand sign (fist with only pinkie and index stretched out): Disable all other hand recognition signs.
- "Love" Hand sign (Rock and Roll but with thumb stretched out): Toggle on all other hand recognition signs.





