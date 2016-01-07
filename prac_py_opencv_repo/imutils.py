__author__ = 'mbess'

import numpy as np
import cv2

# create translation matrix "M"
# first row specifies the number of pixels shifted
# left or right. negative values left, positive right
# Likewise second row specifies pixels shifted up or down
# negative shifts up, positive down


def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[ : 2]

    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def resize(image, width=None, height=None,
           inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        # calculate aspect ratio of height
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        # calculate aspec ratio of width
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim,
                         interpolation = inter)
    return resized