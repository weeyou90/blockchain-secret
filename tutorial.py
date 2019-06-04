import cv2
from matplotlib import pyplot as plt
import numpy as np

# # Showing images
# 
# The function/method cv2.imshow() lets us display an image in a window which fits itself to the size of the image.


#load
img1 =cv2.imread('spiderman.jpeg', cv2.IMREAD_COLOR) #default flag. neglect transparency
img2 =cv2.imread('spiderman.jpeg', cv2.IMREAD_GRAYSCALE) #greyscale
img3 =cv2.imread('spiderman.jpeg', cv2.IMREAD_UNCHANGED) #include alpha channel

# show, wait, destroy
cv2.imshow('Python1',img1)
cv2.imshow('Python2',img2)
cv2.imshow('Python3',img3)
cv2.waitKey(0) # press any key to destroy all windows

#cv2.destroyWindow('Python1') #make sure window closes cleanly
cv2.destroyAllWindows() #destroy all windows
