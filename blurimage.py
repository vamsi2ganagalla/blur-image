import cv2
cap=cv2.VideoCapture(0)
model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#connecting all the strings and making the image into a video
while True:
    ret,photo=cap.read()
    face=model.detectMultiScale(photo)
    if len(face)==0:
        print("no face")
    else:
        x1=face[0][0]
        y1=face[0][1]
        x2=face[0][2]+x1
        y2=face[0][3]+y1
        rphoto=cv2.rectangle(photo,(x1,y1),(x2,y2),[0,0,255],2)
        cphoto=photo[y1:y2,x1:x2]
        bphoto=cv2.blur(cphoto,(10,10))
        photo[y1:y1+bphoto.shape[0],x1:x1+bphoto.shape[1]]=bphoto
        cv2.imshow('hi',photo)
        if cv2.waitKey(100)==13:
            break
cv2.destroyAllWindows()
