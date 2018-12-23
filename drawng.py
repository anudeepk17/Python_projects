import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(511,511),(200,120,34),5)
cv2.rectangle(img,(0,0),(40,40),(17,6,98),2)
cv2.circle(img,(447,63),63,(200,100,0),-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,200,120))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img)
