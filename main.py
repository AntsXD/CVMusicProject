import face_recognition
import face_recognition_models
import numpy as np
import cv2 as cv
import pygame.mixer_music



    

music_started= False

cap = cv.VideoCapture(0)
#must init mixer always
pygame.mixer.init()
#this will later be a bunch of random songs
pygame.mixer.music.load(r"music/CryForMe.mp3")
pygame.mixer.music.set_volume(0.6)
#tried putting this in the while loop but the music doesnt play if im in the while loop
#pygame.mixer.music.play()

if not cap.isOpened():
    print("Cannot Open")
    exit()


while True:
    #later on this only plays when the face is detected
    #pygame.mixer.music.play()
    #claude suggested i do this:
    #this works because now its separate from the while loop, it used to restart every iteration, now it doesn't
    #if not pygame.mixer.music.get_busy():
    #pygame.mixer.music.play()

    # ret is a boolean value that returns true if a frame is captured
    ret, frame = cap.read();

   

    if not ret:
        print("Frame error")
        break


  
    
    face_locations = face_recognition.face_locations(frame)

    #trying to tie in face logic to music
 
    if face_locations != []:  # Face detected
        if not music_started:
            pygame.mixer.music.play()
            music_started = True
        else:
            pygame.mixer.music.unpause()
    else:  # No face detected
        pygame.mixer.music.pause()

    for face_location in face_locations:

    # Print the location of each face in this image
        top, right, bottom, left = face_location
        cv.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 3)

    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'): #this is in the documentation but idk what it means
        #ah turns out it is just a way to exit by clicking q, cool
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        break


#must kill capture before quitting program
cap.release()
cv.destroyAllWindows()
