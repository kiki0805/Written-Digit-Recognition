# USAGE
# python detect_circles.py --image images/simple.png

# import the necessary packages
import numpy as np
import argparse
import cv2
from PIL import Image
import cv2.cv as cv
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image, clone it for output, and then convert it to grayscale
im = Image.open(args["image"])
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles in the image
circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT,2,60,50,60,50,25)
center_list = []
r_list = []
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")

	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		if r < 45 and x >100 and x < 300 and y >30 and y < 150:
		#r > 100 and r < 170 and x < 1300 and x > 400 and y < 700:
			center_list.insert(0,(x,y))
			r_list.insert(0,r)
			#print r
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			#print x,y
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	print "in"
	# show the output image
	#cv2.imshow("output", np.hstack([image, output]))
	cv2.imwrite("ou.png",output)
	cv2.waitKey(0)
	count = 0
	for i in center_list:
		x_ = i[0]
		y_ = i[1]
		r_ = r_list[0]
		im2 = im.crop((x_ - r_, y_ - r_, x_ + r_, y_ +r_))
		im2.save("result"+str(count)+".png")
		count = count + 1
