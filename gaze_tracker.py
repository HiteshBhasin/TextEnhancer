import cv2
from cvzone.PoseModule import PoseDetector
import sys
videoframe = cv2.VideoCapture(0)
detector  = PoseDetector()
if videoframe.isOpened()==False:
    sys.exit("Error: Could not open video capture.")

while videoframe.isOpened():
    ret , frame = videoframe.read()
    if ret==False:
        break
    else:
        frame =detector.findPose(frame, True)
        lmList, box = detector.findPosition(frame,True )
        print(lmList)
        cv2.imshow("Image", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
videoframe.release()
cv2.destroyAllWindows()