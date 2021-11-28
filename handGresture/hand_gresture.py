import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, +1)

    # to mirror image frame to become easy for writing
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    # lower bound threshold
    lb= np.array([0, 0, 81])
    # upper bound threshold
    ub = np.array([185, 255, 255])

    # keep values lying between lb and ub and discard the rest of the values.
    mask = cv2.inRange(frame2, lb, ub)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
