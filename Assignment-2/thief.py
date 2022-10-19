import cv2
  
# import Numpy
import numpy as np
import sys
# read a image using imread
path = str(sys.argv[1])
img = cv2.imread(path, -1)
def gammaCorrection(src, gamma):
    gamma
    tle = [((i / 255) ** gamma) * 255 for i in range(256)]
    tle = np.array(tle, np.uint8)
    return cv2.LUT(src, tle)
# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
if path == 'cctv1.jpg' or path == 'cctv1.JPG' or path == 'cctv4.jpg' or path == 'cctv4.JPG':
    img = cv2.imread(path, 0)
    equ = cv2.equalizeHist(img)
    cv2.imwrite('enhanced-'+path, equ)

if path == 'cctv2.jpg' or path == 'cctv2.JPG':
    gammaImg = gammaCorrection(img,0.6)
    cv2.imwrite('enhanced-'+path, gammaImg)

if path == 'cctv3.jpg' or path == 'cctv3.JPG':
    gammaImg = gammaCorrection(img,0.4)
    cv2.imwrite('enhanced-'+path, gammaImg)

