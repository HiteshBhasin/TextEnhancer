import cv2
import pytesseract
from gaze_tracker import eye_gazer
# the statement below is important for tesseract engine to run.
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



# converting the image into grescale



def greyColor(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# removing the noise
'''
The remove_noise function applies a median blur to the input image using OpenCV's cv2.medianBlur method. 
Median blurring is a noise-reduction technique that replaces each pixel's value with the median value of the pixel's neighborhood. 
This is particularly effective for removing "salt-and-pepper" noise while preserving edges in the image. 
The second argument, 5, specifies the size of the kernel (a 5x5 window), which determines the neighborhood size used for calculating the median. 
Larger kernel sizes result in stronger smoothing but may also blur fine details.
'''
def remove_noise(img):
    return cv2.medianBlur(img,5)

# threshholding 
'''
The threshholding function performs thresholding on the input image using OpenCV's cv2.threshold method. 
Thresholding is a binarization technique that converts an image into a binary format (black and white) based on a threshold value. 
In this case, the function uses cv2.THRESH_BINARY + cv2.THRESH_OTSU. The cv2.THRESH_BINARY flag sets pixels to either 0 (black) or 255 (white) depending on whether their intensity is below or above the threshold. 
The cv2.THRESH_OTSU flag automatically determines the optimal threshold value by analyzing the image's histogram, making it particularly useful for images with varying lighting conditions. The function returns a tuple, but only the second element (the thresholded image) is returned here.
'''
def threshholding(img):
    return cv2.threshold(img, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

'''
Together, these functions are likely part of a preprocessing pipeline to clean up and prepare images for further analysis, such as extracting text using OCR. 
The remove_noise function ensures the image is free of noise, while the threshholding function simplifies the image into a binary format, making it easier for OCR algorithms to detect and recognize characters
'''


def ocr_core(img):
    img = greyColor(img)
    img = threshholding(img)
    img = remove_noise(img)
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread('textImage.png')
print(ocr_core(img))