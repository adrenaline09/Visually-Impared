import cv2
import numpy as np
import time
from espeak import espeak
import datetime
import pytesseract
img_cv = cv2.imread(r'/home/pi/pytesseract/tests/data/test.png')

previous ="unknown"

video_capture = cv2.VideoCapture(0)

process_this_frame = True

while True:
   
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color 
    rgb_small_frame = small_frame[:, :, ::-1]

    
    if process_this_frame:

        cv2.imwrite('/home/pi/pytesseract/tests/data/test.png', frame)
        img_cv = cv2.imread(r'/home/pi/pytesseract/tests/data/test.png')
        

        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        print(pytesseract.image_to_string(img_rgb))
        espeak.set_voice("En")
        espeak.synth("Hey hello ")
        espeak.synth(pytesseract.image_to_string(img_rgb))
        
        cv2.imshow('Video', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
bus.close()
cv2.destroyAllWindows()
