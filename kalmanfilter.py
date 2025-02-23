import cv2
import numpy as np


kalman = cv2.KalmanFilter(4, 2) #the 4 indicates 4 states being (x,y, velocity x, velocity y), The 2 indiocate the measuremnts of x and y


# State transition matrix
kalman.transitionMatrix = np.array([
    [1, 0, 1, 0],  # x = x + vx * dt
    [0, 1, 0, 1],  # y = y + vy * dt
    [0, 0, 1, 0],  # vx = vx
    [0, 0, 0, 1]  # vy = vy
], np.float32)

# 1. Row 1 updates the x-position: Where the hand will be horizontally depends on where it is now and how fast it’s moving horizontally.
# 2. Row 2 updates the y-position: Where the hand will be vertically depends on where it is now and how fast it’s moving vertically.
# 3. Row 3 updates the x-velocity: How fast the hand is moving horizontally doesn’t change unless something else affects it.
# 4. Row 4 updates the y-velocity: How fast the hand is moving vertically doesn’t change unless something else affects it.


# Measurement matrix
kalman.measurementMatrix = np.array([
    [1, 0, 0, 0],  # Measure x
    [0, 1, 0, 0]  # Measure y
], np.float32)

# Process noise covariance matrix
kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 1e-2

# Measurement noise covariance matrix
kalman.measurementNoiseCov = np.eye(2, dtype=np.float32) * 1e-1

# Error covariance post matrix
kalman.errorCovPost = np.eye(4, dtype=np.float32)

# Initialize state (x, y, vx, vy) to zeros
kalman.statePost = np.zeros((4, 1), np.float32)

# kalman.measurementNoiseCov *= 10


def kalman_filter(x,y, noise):
    global kalman
    kalman.measurementNoiseCov = np.eye(2, dtype=np.float32) * 1e-1
    kalman.measurementNoiseCov *= (noise * 2)
    predicted_state = kalman.predict()
    predicted_x, predicted_y = predicted_state[0], predicted_state[1]
    measurement = np.array([[x], [y]], dtype=np.float32)

    if x is not None and y is not None:
        measurement = np.array([[np.float32(x)], [np.float32(y)]], dtype=np.float32)
        corrected_state = kalman.correct(measurement)
        corrected_x, corrected_y = corrected_state[0], corrected_state[1]
    else:
        corrected_x, corrected_y = predicted_x, predicted_y

    return corrected_x, corrected_y


