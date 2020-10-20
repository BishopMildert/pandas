# Importing packages
from Transform.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils



# argument parser
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image to be scanned')
args =vars(ap.parse_args())


# load image and compute ratio of old height
# to new hight, clone it and resize it

image = cv2.imread(args['image'])
ratio = image.shape[0] / 500.
orig = image.copy()
image = imutils.resize(image, height=500)

# convert image to greyscale, gausian blur and endge detection
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey = cv2.GaussianBlur(grey, (5,5), 0)
edge = cv2.Canny(grey, 75, 200)

# show original image and edge detect image
print('STAGE 1: Edge Dection')
cv2.imshow('IMAGE', image)
cv2.imshow('EDGE', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

# look for contour in the edged image
cnts = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

# looping over the contours
for c in cnts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # if the approx contour has 4 points we can assume the receipt area has been found
    if len(approx) == 4:
        screenCnt = approx
        break

    

# show image with outline of receipt
print('STEP 2: Find Outline of Receipt')
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow('Outline', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply the 4 point transformation
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

# convert the transformed image into greyscale
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset=10, method='gaussian')
warped = (warped > T).astype('uint8') * 255

# show original and scanned images
print('STEP 3: SCANNING IMAGE')
cv2.imshow('Original', imutils.resize(orig, height=650))
cv2.imshow('Scanned', imutils.resize(warped, height=650))
cv2.waitKey(0)
cv2.destroyAllWindows()