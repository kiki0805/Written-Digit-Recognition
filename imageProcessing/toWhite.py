from PIL import Image
import cv2.cv as cv
import cv2
import numpy as np
import time
import math
import string
import os
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

im = cv.LoadImage(args["image"])
im2 = Image.open(args["image"])
side = im2.size[0]
side2 = im2.size[1]
for i in range(side):
    for j in range(side2):
        #print i,j
        color = im[j,i]
        if color[2] >= 170 or color[1] >= 140 or color[0] >= 90:
            im[j,i] = (255,255,255)
        else:
            im[j,i] = (0,0,0)
cv.SaveImage(args["image"][0:7]+"_f.png",im)
