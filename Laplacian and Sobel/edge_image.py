# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 18:48:32 2018

@author: HP
"""
import numpy as np
import cv2
image = cv2.imread("image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Original Image | Laplacian", np.hstack([image, lap]))
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X | Sobel Y | Sobel Combined", np.hstack([sobelX, sobelY, sobelCombined]))
cv2.waitKey(0)
