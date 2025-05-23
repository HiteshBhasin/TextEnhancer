import cv2
import dlib 

face_detection = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
def eye_gazer(camera):

    videoframe = camera.VideoCapture(0)
    
    while True:
        success , frame = videoframe.read()
        
        if success:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_detection(gray)
         
            for face in faces:
                landmark = predictor(gray,face) 
                left_x = landmark.part(41).x
                left_y = landmark.part(36).y
                right_x = landmark.part(46).x
                right_y = landmark.part(45).y
                return left_x,left_y, right_x, right_y
                
                
            camera.imshow("frame", frame)  
        if camera.waitKey(1) & 0xFF == ord('q'):
                break
        
            
    videoframe.release()
    cv2.destroyAllWindows()
print(eye_gazer(cv2))
#  still need to return the directions and relate it to rectangle