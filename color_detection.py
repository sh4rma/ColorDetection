import cv2 # computer vision version 2
import numpy as np # yeh array ko store karne ke liye kiya jaata hai

# Initialize webcam
cap = cv2.VideoCapture(0)  # yeh method hai

# Red color range in HSV
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mask to detect red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND the mask and the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show the frames
    cv2.imshow('Original', frame)
    cv2.imshow('Detected Color', result)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
