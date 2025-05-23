import cv2
import dlib 

face_detection = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

print(predictor)
def eye_gazer(camera):

    videoframe = camera.VideoCapture(0)
    
    while True:
        success , frame = videoframe.read()
        
        if success:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_detection(gray)
         
            for face in faces:
                landmark = predictor(gray,face) 
                left_x = landmark.part().x
                left_y = landmark.part(39).y
                cv2.rectangle(frame,(left_x,left_y),3, (255,0,0),3)
                print(left_x,left_y)
                
            camera.imshow("frame", frame)  
        if camera.waitKey(1) & 0xFF == ord('q'):
                break
        
            
    videoframe.release()
    cv2.destroyAllWindows()
eye_gazer(cv2)
#  still need to return the directions and relate it to rectangle