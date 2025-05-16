import pyautogui 
import time

def AutoScroll(path, coordinates):
    x, y = coordinates
    with open(path ,'r') as file:
        lines = file.readlines()
    
    for line in lines:
        print(line.strip())
        pyautogui.scroll(y)
        time.sleep(3)    
    
    file.close()
    


        