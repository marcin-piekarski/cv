# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 09:34:22 2014
twitter feed parser
@author: mbess
"""
from PIL import Image
import os
from pylab import *


def get_imList(path):
    return [f for f in os.listdir(path) if f.endswith('.jpg')]


def showContours(path):

    # read image to array
    im = array(Image.open(path).convert('L'))

    # create figure
    figure(1)

    # dont' use colors
    gray()

    # show contours
    contour(im, origin='image')
    axis('equal')

    figure(2)
    gray()
    hist(im.flatten(),128)
    