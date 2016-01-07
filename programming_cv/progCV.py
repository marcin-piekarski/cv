# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:29:36 2014

@author: mbess
"""

from PIL import Image
from pylab import *
import imtools

# get ist of jpg images 
imList = imtools.getImList('C:\\Users\\mbess\\Dropbox\\car\\')

# open first image
im = array(Image.open(imList[0]).convert('L'))

# create a figure
figure()

# show contour no color
contour(im, origin='image')
