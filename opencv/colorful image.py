import numpy as np
import cv2
img=np.ones([400,400,3],dtype=np.uint8)
img[0:400,0:400]=[114,255,125]
print(img)
print(img.dtype)
cv2.imshow('Output',img)
cv2.waitKey()
cv2.destroyAllWindows()
