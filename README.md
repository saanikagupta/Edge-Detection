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

## The Canny Edge Detector
The Canny edge detector is a multi-step process. It involves blurring the image to remove noise, computing Sobel gradient images in the x and y direction, suppressing edges, and ﬁnally a hysteresis thresholding stage that determines if a pixel is “edge-like” or not.

## Execution for detecting edges in an image (Laplacian and Sobel)
To run the code, type `python edge_image.py`

### Output
![capture1](https://user-images.githubusercontent.com/33591235/50455603-23535c00-0975-11e9-95d1-634618738fdd.PNG)

## Execution for real-time edge detection (Laplacian and Sobel)
To run the code, type `python edge_webcam.py`

### Output
![capture3](https://user-images.githubusercontent.com/33591235/50455700-e045b880-0975-11e9-8216-0954f4d08597.PNG)
![capture4](https://user-images.githubusercontent.com/33591235/50455715-f3f11f00-0975-11e9-813b-604504590132.PNG)

## Execution for Canny Edge Detection in real-time
To run the code, type `python canny_edge.py`

### Output
![capture4](https://user-images.githubusercontent.com/33591235/50479618-7670f180-09fd-11e9-9686-a7bd8696ac22.PNG)
