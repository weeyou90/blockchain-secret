import cv2
from matplotlib import pyplot as plt
import numpy as np


# # Edge detection using Canny

# In[10]:


edge=cv2.imread('spiderman.jpeg')
cv2.imwrite('edge_spidey.jpg',cv2.Canny(edge,512,512))
cv2.imshow('edges',cv2.imread('edge_spidey.jpg'))

cv2.waitKey(0)
cv2.destroyAllWindows() #destroy all windows

