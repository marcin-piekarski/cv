# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:21:02 2014

@author: mbess
"""

import os
from PIL import Image
from pylab import *

path = r'c:\Users\mbess\Git\cv\data\car\CAZT6FD5.jpg'
path2 = r'/home/naphazg/Dropbox/cv/data/car/CAZT6FD5.jpg'

def main():
    im = Image.open(path)
    bound_box = im.getbbox()  # left, top, right, bottom
    px_rgb = list(im.getdata())  # [pixel(r,g,b), ...]
    px_rgb_cnt = im.getcolors(maxcolors=50000)  # 50k a guess, half pixel count
    