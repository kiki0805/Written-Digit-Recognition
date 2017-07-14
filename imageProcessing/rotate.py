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

y_range = 5
y_proportion = 0.2
x_proportion = 0.6
global im,sum_rotate
im=Image.open(args["image"])
im = im.convert("RGB")
sum_rotate = 0
def rotate(img):
    global im,sum_rotate
    length = img.size[0]
    height = img.size[1]
    top_bound = height - round(height * y_proportion) - y_range
    down_bound = height - round(height * y_proportion) + y_range
    left_bound = round(length * (1 - x_proportion))
    right_bound = round(length * x_proportion)
    coff = 1
    im_ = img
    flag = 0
    #print top_bound,down_bound
    #print left_bound,right_bound
    c = [0]
    while 1:
        i = top_bound
        j = left_bound
        count = 0
        while i < down_bound:
            while j < right_bound:
                color = im_.getpixel((j,i))
                #print color
                if color[0] > 150 and color[1] < 150 and color[2] < 100:
                    count = count + 1
                j = j + 1
            i = i + 1
            j = left_bound
        c.insert(0, count)
        if count == 0:
            count = 1
        if c[0] < c[1] and c[0] != 1:
            break
        im_ = im.rotate(sum_rotate, resample=Image.BICUBIC)
        sum_rotate = sum_rotate + 10
        #print sum_rotate, count
        #im_.save('res.png')
        #time.sleep(5)
        if abs(sum_rotate) > 360:
            break
    return count, im_
length = im.size[0]
d, i = rotate(im)
a = int(length-0.75*length)
b = int(length-0.25*length)
i = i.crop((a,a,b,b))
i.save('result_'+args["image"][0:-4]+'.png')
