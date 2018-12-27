# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:33:15 2018

@author: HP
"""
import imutils
import numpy as np 
import cv2

camera = cv2.VideoCapture(0)
while True:
    (ret, frame) = camera.read()
    frame = imutils.resize(frame, width = 600)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image, (5, 5), 0) 
    canny = cv2.Canny(image, 30, 150)
    cv2.imshow("Gaussian blurred grayscale image | Canny edge detector", np.hstack([image, canny]))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()