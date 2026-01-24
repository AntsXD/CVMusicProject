import face_recognition
import face_recognition_models
import numpy as np
import cv2 as cv
import pygame.mixer_music
import random


music_list = [
    r"music/CryForMe.mp3",
    r"music/Timeless.mp3",
    r"music/CryForMe.mp3",
    r"music/BaptizedInFear.mp3"
]

random_song = random.choice(music_list)



    

music_started= False
friend_detected = False

image = face_recognition.load_image_file(r"imgs/ID.jpeg")
image_encoding = face_recognition.face_encodings(image)[0]

cap = cv.VideoCapture(0)
#must init mixer always
pygame.mixer.init()
#this will later be a bunch of random songs
#bunch of songs added
pygame.mixer.music.load(random_song)
pygame.mixer.music.set_volume(0.6)
#tried putting this in the while loop but the music doesnt play if im in the while loop
#pygame.mixer.music.play()

if not cap.isOpened():
    print("Cannot Open")
    exit()


while True:
    #must add this so that the music can stop else it will go infinitely
    friend_detected = False
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
 
    # if face_locations != []:  # Face detected
    #     #needed to use music_started variable just to be able to differentiate between play and unpause state, so the .get_busy() is no longer needed 
    #     if not music_started:
    #         pygame.mixer.music.play()
    #         music_started = True
    #     else:
    #         pygame.mixer.music.unpause()
    # else:  # No face detected
    #     pygame.mixer.music.pause()

    


    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations,face_encodings):
        matches = face_recognition.compare_faces([image_encoding],face_encoding)
        name = "Unknown"
        if matches[0]:
            name = "Ants"
            #using this for the music player
            friend_detected = True
            cv.rectangle(frame,(left,top),(right,bottom),(255,0,0),3)
            cv.putText(frame,name,(left,top-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
            break

     #now the music only plays if this the exact face       
    if friend_detected:  # Face recognized
        #needed to use music_started variable just to be able to differentiate between play and unpause state, so the .get_busy() is no longer needed 
        if not music_started:
            pygame.mixer.music.play()
            music_started = True
        else:
            pygame.mixer.music.unpause()
    else:  # No face detected
        pygame.mixer.music.pause()





    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'): #this is in the documentation but idk what it means
        #ah turns out it is just a way to exit by clicking q, cool
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        break


#must kill capture before quitting program
cap.release()
cv.destroyAllWindows()
