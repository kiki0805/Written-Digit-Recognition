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

def check_row(img,side, row_num):
    #print row_num
    oneline = cv.GetRow(img, row_num)
    for i in range(side):
        color = oneline[0,i]
        #print color
        if color[2] < 170 and color[1] < 140 and  color[0] < 90:
            return 0
    return 1
def check_col(img,side,col_num):
    oneline = cv.GetCol(img, col_num)
    #print oneline
    for i in range(side):
        color = oneline[i,0]
        if color[2] < 170 and color[1] < 140 and  color[0] < 90:
            return 0
    return 1
im = cv.LoadImage(args["image"])
im2 = Image.open(args["image"])
oneline = cv.GetRow(im, 0)
side = im2.size[0]
side2 = im2.size[1]
row_index = 0
#print side
while check_row(im, side2, row_index) != 0:
    row_index = row_index + 1
row_index2 = side2 - 1
while check_row(im, side2, row_index2) != 0:
    row_index2 = row_index2 - 1
col_index = 0
while check_col(im, side, col_index) != 0:
    col_index = col_index + 1
col_index2 = side - 1
while check_col(im, side, col_index2) != 0:
    col_index2 = col_index2 - 1
diff_row = row_index2 - row_index
diff_col = col_index2 - col_index

if diff_row >= diff_col:
    col_index = col_index - (diff_row - diff_col) / 2
    col_index2 = col_index2 + (diff_row - diff_col) / 2
else:
    row_index = row_index - (diff_col - diff_row) / 2
    row_index2 = row_index2 + (diff_col - diff_row) / 2

im2 = im2.crop((int(col_index),int(row_index),int(col_index2),int(row_index2)))
im2.save(args["image"][-11:-4]+"_c.png")
