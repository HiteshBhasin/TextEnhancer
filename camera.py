import cv2 as capture
from ocr_processor import ocr_core
import numpy as np # this is to make the box inside the capture.
import os
from AutoScroll import AutoScroll

def videoCapturing():
    videoCapture = capture.VideoCapture(0)
    if (videoCapture.isOpened()==False):
        print("error!")
    
    start_point = (50,100)
    end_point = (600,200)
    color = (0,255,0)
    thickness= 2
    if not os.path.exists('Document.txt'):
         open('Document.txt', 'w').close()
    
    file = open('Document.txt','a')
    while videoCapture.isOpened():
  
        x1 ,y1 = start_point
        x2,y2 = end_point
        ret, frame = videoCapture.read()
        crop = frame[y1:y2,x1:x2]
        text = ocr_core(crop)
        file.write(text)
        if ret==True:
            capture.rectangle(frame,start_point,end_point,color,thickness)
            capture.imshow('cropFrame', crop)
            if capture.waitKey(1) & 0xFF==27:
                break
        else:
            break
    videoCapture.release()
    capture.destroyAllWindows()    

