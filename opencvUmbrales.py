import cv2
import numpy as np


opencv = cv2.imread("./img/sudoku.png")
gris = cv2.cvtColor(opencv, cv2.COLOR_BGR2GRAY)
gris = cv2.GaussianBlur(gris, (7,7), 0)
bin = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#ret, bin = cv2.threshold(gris, 80, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("SUDOKU", bin)

cv2.waitKey(0)
   # cv2.destroyAllWindows()