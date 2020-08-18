import cv2
# face classifier
face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector=cv2.CascadeClassifier('haarcascade_smile.xml')
#grab webcam feed
webcam=cv2.VideoCapture(0)


while  True:
    #read single frame
    suuccesful_frame_read,frame=webcam.read()

    #if cm is not check
    if not suuccesful_frame_read:
        break

    #change to grayscale(black and white)
    #this is to optimization
    frame_grayscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_detector.detectMultiScale(frame_grayscale)
    # smiles=smile_detector.detectMultiScale(frame_grayscale,scaleFactor=1.7,minNeighbors=20)


    #creating rectangle around faces
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(100,200,50),4)
        #find all smile in face in exah of face which we find in
        #get the sub array (using numpy n -deimensyional array slicing)
        the_face=frame[y:y+h,x:x+w]
        # the_face=(x,y,w,h)
        face_grayscale=cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)
        the_face_smile=smile_detector.detectMultiScale(face_grayscale,scaleFactor=1.7,minNeighbors=20)
        if len(the_face_smile)>0:
            cv2.putText(frame,'smiling',(x,y+h+40),fontScale=3,
            fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))
        for(x_,y_,w_,h_)  in the_face_smile:
            cv2.rectangle(the_face,(x_,y_),(x_+w_,y_+h_),(50,50,200),4)
            

    #to detect smile in whole frame
    # for(x,y,w,h) in smiles:
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,200),4)

    

    #to show captured frame
    cv2.imshow('why so serious',frame)

    #tro capture frame on each key
    #providing 1 it will call wait key in milli seconds
    cv2.waitKey(1)
    #show the current frame

#to cleanup and release resource
webcam.release()
cv2.destroyAllWindows()


print("whats up")