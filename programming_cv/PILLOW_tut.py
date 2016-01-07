# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 11:50:11 2014

@author: mbess
"""
from __future__ import print_function
import os, sys
from PIL import Image


iPath = "C:/Users/mbess/Git/cv/data/car/"

#convert file to JPG
for infile in os.path("C:/Users/mbess/Git/cv/data/car/CAFU8YND.jpg"):
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
            
size = (128, 128)

for infile in os.path("C:/Users/mbess/Git/cv/data/car/CAFU8YND.jpg"):
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
            print("created thumbnail for ", infile)
        except IOError:
            print("cannot create thumbnail for ", infile)
