import cv2
import numpy as np

img = np.zeros((250, 250, 3), np.uint8)

cv2.line(img, (50,50), (200,200), (0,255,0), 2)
cv2.rectangle(img, (70, 130), (100, 200), (250, 0, 0), -1)
cv2.circle(img, (125,125), 70, (0,0,255), 7)

vertices = np.array([ [[20,30]], [[50,150]], [[200,15]], [[60,60]], [[150,50]] ])
cv2.polylines(img, [vertices], False, (0, 255, 255), 6)

cv2.imshow("Dibujo", img)

cv2.waitKey(0)
cv2.destroyAllWindows()