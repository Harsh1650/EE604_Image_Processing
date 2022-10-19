import cv2
import numpy as np
import sys
sigma = 0.33
# Read image
path = str(sys.argv[1])
image = cv2.imread(path)

# Convert image to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

v = np.median(gray)

lower = int(max(0, (1.0 - sigma) * v))
upper = int(min(255, (1.0 + sigma) * v))
# Use canny edge detection
#We can add lower and Upper for optimal value
edges = cv2.Canny(gray,120,180)
linesarray =[]
lines = cv2.HoughLinesP(
		edges,
		1,
		np.pi/180,
		threshold=90,
		minLineLength=9,
		maxLineGap=60
		)

# Iterate over points
for points in lines:
	# Extracted points nested in the list
	x1,y1,x2,y2=points[0]
	# Draw the lines joing the points
	# On the original image
	cv2.line(image,(x1,y1),(x2,y2),(255,0,255),2)
	# Maintain a simples lookup list for points
	linesarray.append([(x1,y1),(x2,y2)])
	
# Save the result image
cv2.imwrite('robolin-'+path,image)