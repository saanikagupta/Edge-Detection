# Edge-Detection
Formally, edge detection embodies mathematical methods to ﬁnd points in an image where the brightness of pixel intensities changes distinctly.

## Code Requirements
The code is in Python (version 3.6 or higher will work).

## Dependencies
- import cv2
- import imutils
- import numpy

## Description
### The Sobel Edge Detector
Using the Sobel operator, we can compute gradient magnitude representations along the x and y axis, allowing us to ﬁnd both horizontal and vertical edge-like regions.

### The Laplacian Edge Detector
The Laplacian edge detector uses only one kernel. It calculates second order derivatives in a single pass. Working with second order derivatives, the laplacian edge detector is extremely sensitive to noise. Gaussian blur can be used to reduce noise. Laplacians are computationally faster to calculate (only one kernel vs two kernels).

## Execution for detecting edges in an image
To run the code, type python `edge_image.py`

## Execution for real-time edge detection
To run the code, type python `edge_webcam.py`




