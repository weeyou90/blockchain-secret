import cv2
from matplotlib import pyplot as plt
import numpy as np


# # Face Detection
# https://docs.opencv.org/3.1.0/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0

# In[29]:


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

img=cv2.imread('me.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting it to grayscale
faces=face_cascade.detectMultiScale(img,1.3,5) #Performing the detection

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows() #destroy all windows

