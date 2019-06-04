import cv2
from matplotlib import pyplot as plt
import numpy as np

img2 =cv2.imread('spiderman.jpeg', cv2.IMREAD_GRAYSCALE) #greyscale
#write to a new file
cv2.imwrite('grey.png',img2)

#display using matplotlib
plt.imshow(img2,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()

