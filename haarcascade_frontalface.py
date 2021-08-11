#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 11:02:00 2021

@author: tejasripattapu
"""

	
import cv2
import numpy as np
import math
img=cv2.imread("pic.jpg")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
while 1:
  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    cv2.imshow("Image",img)
    k = cv2.waitKey(30) & 0xff
  if k == 27:
    break
cv2.destroyAllWindows()