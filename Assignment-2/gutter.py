import cv2
import numpy as np
import sys
path = str(sys.argv[1])
def gammaCorrection(src, gamma):
    gamma
    tal = [((i / 255) ** gamma) * 255 for i in range(256)]
    tal = np.array(tal, np.uint8)
    return cv2.LUT(src, tal)
im = cv2.imread(path)
# cv2.imshow("Original",im)
# cv2.imshow("crop",im)
im1 = cv2.medianBlur(im,21)
# cv2.imshow("blur",im1)
im2 = 255- cv2.absdiff(im,im1)
# cv2.imshow("Diff",im2)
im3 = cv2.normalize(im2, im2, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
# cv2.imshow("Show",im3)
cv2.imwrite('cleaned-gutter.jpg',im3)

