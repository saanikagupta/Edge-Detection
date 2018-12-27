# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 18:48:32 2018

@author: HP
"""
import imutils
import numpy as np
import cv2

camera = cv2.VideoCapture(0)
while True:
    (ret, frame) = camera.read()
    frame = imutils.resize(frame, width = 300)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(image, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    
    sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobelCombined = cv2.bitwise_or(sobelX, sobelY)
    cv2.imshow("Grayscale original | Laplacian", np.hstack([image, lap]))
    cv2.imshow("Sobel X | Sobel Y", np.hstack([sobelX, sobelY]))
    cv2.imshow("Sobel Combine", sobelCombined)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()

