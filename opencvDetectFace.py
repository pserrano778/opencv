import cv2
import numpy as np

facexml = "./DetectFace/haarcascade_frontalface_default.xml"
smilexml = "./DetectFace/haarcascade_smile.xml"
cc_cara = cv2.CascadeClassifier(facexml)
cc_smile = cv2.CascadeClassifier(smilexml)

camara = cv2.VideoCapture(0)
img = cv2.imread("./img/billar.jpg")

while camara.isOpened() is True:

   ret,frame = camara.read()

   if ret is True:
      gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      caras = cc_cara.detectMultiScale(gris, scaleFactor=1.4, minNeighbors = 2, minSize=(90,90))

      for(cx,cy,cw,ch) in caras:
         cv2.rectangle(frame, (cx,cy), (cx+cw,cy+ch), (0,255,0),2)
         sonrisas = cc_smile.detectMultiScale(gris[cy:cy+ch, cx:cx+cw], scaleFactor=2, minNeighbors = 2, minSize=(30,30))
         for(sx,sy,sw,sh) in sonrisas:
               cv2.rectangle(frame, (cx+sx,cy+sy), (cx+sx+sw, cy+sy+sh), (255,0,0),2)

      cv2.imshow("Caras", frame)
      if cv2.waitKey(20) == ord(' '):
         break
camara.release();
cv2.destroyAllWindows()