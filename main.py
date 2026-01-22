import face_recognition
import face_recognition_models
import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot Open")
    exit()


while True:
    # ret is a boolean value that returns true if a frame is captured
    ret, frame = cap.read();

    if not ret:
        print("Frame error")
        break

    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'): #this is in the documentation but idk what it means
        #ah turns out it is just a way to exit by clicking q, cool
        break


#must kill capture before quitting program
cap.release()
cv.destroyAllWindows()
