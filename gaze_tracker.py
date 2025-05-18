import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import sys
def directions(eye_tractor):
    left  = eye_tractor['left']
    right = eye_tractor['right']
    top = eye_tractor['up']
    bottom = eye_tractor['down']
    center = eye_tractor['center']
    
    width = left[0]-right[0]
    height = bottom[1]-top[1]
    
    x_ratio = (center[0]-left[0])/width
    y_ratio = (center[1]-top[1])/height
    
    direction = "center"
    if x_ratio<0.4:
        direction = "left"
    if x_ratio>0.6:
        direction="right"
    if y_ratio<0.4:
        direction+="up"
    if y_ratio >0.6:
        direction+="down"
    
    return direction




def eye_gazer():
    detector  = FaceMeshDetector()
    videoframe = cv2.VideoCapture(0)
    
    while True:
        success , frame = videoframe.read()
        frame, faces =detector.findFaceMesh(frame, True)
        if faces:
            face = faces[0]
            left_eye = {
                "top":face[159],
                "bottom":face[23],
                "left": face[130],
                "right":face[243],
                "center":face[468]
            }
            
            right_eye = {
                "top":face[386],
                "bottom":face[253],
                "left": face[463],
                "right":face[359],
                "center":face[473]
            }

            cv2.circle(frame, left_eye['center'], 3, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, right_eye['center'], 3, (255, 0, 255), cv2.FILLED)
            
            left_direction = directions(left_eye)
            right_direction = directions(right_eye)
            
            cv2.imshow("Eye Gazer", frame)
                
            # cv2.imshow("Image", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    videoframe.release()
    cv2.destroyAllWindows()
eye_gazer()
#  still need to return the directions and relate it to rectangle