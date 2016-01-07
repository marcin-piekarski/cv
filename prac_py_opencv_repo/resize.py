__author__ = 'mbess'

import numpy as np
import argparse
import imutils
import cv2

# configure argument parser
# path to image only argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)


# print "image ratio is: %d / %d = %f" % (150, image.shape[1], r)
# print r

# resize width
resized = imutils.resize(image,width=150)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

# resize height
resized = imutils.resize(image, height=50)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)
