import cv2
import numpy as np
d=False
mode=True
ix,iy=(-1,-1)

def nothing(x):
    pass
def draw_circle(event,x,y,flags,param):
    global ix,iy,d,mode
    if event== cv2.EVENT_LBUTTONDOWN:
        d=True
        ix,iy=x,y
    if event== cv2.EVENT_MOUSEMOVE:
        if d==True:
            if param[4]== 1:
                cv2.rectangle(img,(ix,iy),(x,y),param[0:3],-1)
            else:
                cv2.circle(img,(x,y),param[3],param[0:3],-1)
    elif event==cv2.EVENT_LBUTTONUP:
        d=False
        if param[4]==1:
            cv2.rectangle(img,(ix,iy),(x,y),param[0:3],-1)
        else:
            cv2.circle(img,(x,y),param[3],param[0:3],-1)
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('size','image',0,9,nothing)
brush='Circle\nRectangle'
cv2.createTrackbar(brush,'image',0,1,nothing)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(20) &0xff
    if k==27:
        break
    r=cv2.getTrackbarPos('R','image')
    b=cv2.getTrackbarPos('B','image')
    g=cv2.getTrackbarPos('G','image')
    s=cv2.getTrackbarPos('size','image')
    br=cv2.getTrackbarPos(brush,'image')
    cv2.setMouseCallback('image',draw_circle,[b,g,r,s,br])
cv2.destroyAllWindows()
