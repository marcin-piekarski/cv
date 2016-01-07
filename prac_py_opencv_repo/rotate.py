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

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)
