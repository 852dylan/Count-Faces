import cv2
import numpy as np
import dlib

#video capture saved in cap var
cap = cv2.VideoCapture(0)
#gets face coordinates
detector = dlib.get_frontal_face_detector()

while True:
#capture frame by frame
    ret,frame = cap.read() #read()?,ret?
    frame = cv2.flip(frame, 1) #flip()?
    
    #operations on the frame saved in frame
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    #number of faces counter
    i = 0
    for face in faces:
        x = face.left()
        y = face.top()
        x1 = face.right()
        y1 = face.bottom()
        i +=1

        cv2.putText(frame, 'face num' + str(i), (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        print(face ,i)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
