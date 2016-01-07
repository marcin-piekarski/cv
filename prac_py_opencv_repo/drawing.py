
import numpy as np
import cv2
#
# Lines and Rectangles
#

# create matrix
canvas = np.zeros((300, 300, 3), dtype="uint8")

# draw green line from UL to LR
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green, 3)
cv2.imshow("Canvas", canvas)

# draw red 3pt line from LL to UR
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)

# draw green rectangle outline
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)

# draw red rectangle 5pt outline
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)

# draw blue solid rectangle
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#
# Circles
#

# redefine canvas... think erase old canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")

# get canvas center coordinates
(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)

# define white
white = (255, 255, 255)

# draw concentric circles radius r
# spaced 25 units
# 1st one is a dot at 0,0
# a circle r = 0 at 0,0
# think bullseye
for r in xrange(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#
# Random circle drawing
#
for i in xrange(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 300, size = (2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
