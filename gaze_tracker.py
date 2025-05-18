import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import sys
videoframe = cv2.VideoCapture(0)
detector  = FaceMeshDetector()
if videoframe.isOpened()==False:
    sys.exit("Error: Could not open video capture.")

while videoframe.isOpened():
    ret , frame = videoframe.read()
    if ret==False:
        break
    else:
        frame, faces =detector.findFaceMesh(frame, True)
        
        if faces:
            for face in faces:
                leftEyeUpPoint = face[159]
                leftEyeDownPoint = face[23]
                print(leftEyeDownPoint, leftEyeUpPoint)
            
        cv2.imshow("Image", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
videoframe.release()
cv2.destroyAllWindows()