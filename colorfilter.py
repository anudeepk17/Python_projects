import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_green=np.array([150,150,50])
    u_green=np.array([180,255,150])
    mask=cv2.inRange(hsv,l_green,u_green)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    kernel=np.ones((15,15),np.uint8)
    smoothed=cv2.filter2D(res,-1,kernel)
    blur=cv2.GaussianBlur(res,(15,15),0)
    median=cv2.medianBlur(res,15)
    bilateral=cv2.bilateralFilter(res,15,75,75)
    erosion= cv2.erode(mask,kernel,iterations=1)
    dilation= cv2.dilate(mask,kernel,iterations=1)
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    
    
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('blackhat',blackhat)
    
    cv2.imshow('mask',mask)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)
    
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
