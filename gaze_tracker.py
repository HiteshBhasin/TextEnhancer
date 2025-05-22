import cv2
import dlib



def eye_gazer(camera):

    videoframe = camera.VideoCapture(0)
    
    while True:
        success , frame = videoframe.read()
       
                
        camera.imshow("frame", frame)
        if camera.waitKey(1) & 0xFF == ord('q'):
                break
        
            
    videoframe.release()
    cv2.destroyAllWindows()
eye_gazer()
#  still need to return the directions and relate it to rectangle