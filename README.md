# Real-Time Text Enhancer Using OCR and Generative AI
A computer vision tool that captures live video from your webcam, detects a predefined region of interest (ROI), extracts visible text using Tesseract OCR, and optionally enhances it using generative AI (e.g., summarization, translation, or speech synthesis). Designed to run in real-time with a simple modular structure.

# Features
 Live Video Capture with OpenCV
 Real-Time OCR using pytesseract
 Text Logging to a file (Document.txt)
 Modular Design with a separate OCR handler (ocr_core.py)
 AI-Enhanced Summarization (optional via OpenAI GPT)
 Text-to-Speech (TTS) support
 Multilingual Translation (optional via Google Translate API)

# Use Cases
Assistive tools for the visually impaired
Translating printed material (e.g., street signs, documents) in real-time
Real-time subtitle generation or reading aid
Classroom tools for reading projected materials
Hands-free text digitization from books, whiteboards, etc.
Live content enhancement for presentations or videos

#Screenshots


## Here's a simple working base:
python
Copy
Edit
import cv2
import pytesseract

# Set Tesseract path if needed
## (pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe')
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text.strip()

cap = cv2.VideoCapture(0)
start_point = (50, 100)
end_point = (600, 200)
color = (0, 255, 0)
thickness = 2

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    x1, y1 = start_point
    x2, y2 = end_point

    cv2.rectangle(frame, start_point, end_point, color, thickness)
    roi = frame[y1:y2, x1:x2]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    text = ocr_core(gray_roi)
    if text:
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)

    cv2.imshow("Text Enhancer", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Setup Instructions
Install Requirements:
bash
Copy
Edit
pip install opencv-python pytesseract
Install Tesseract-OCR Engine:
Windows installer
On Linux: sudo apt install tesseract-ocr
Run the App:
bash
Copy
Edit
python main.py

# Optional: AI Integration
You can enhance the text output using GPT (via OpenAI API):
python
Copy
Edit
import openai
openai.api_key = 'your-api-key'

# Technologies Used
Python
OpenCV
pytesseract (Tesseract OCR)
OS module (for file writing)
Optional: OpenAI API, pyttsx3 / gTTS, Google Translate
