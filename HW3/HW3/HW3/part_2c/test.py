import cv2
import numpy as np
from skimage.metrics import structural_similarity

img=cv2.imread("frames/1388.png")

template1 = cv2.imread("Fireball.png")

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

prev_max_val1 = 0
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

if cap.isOpened():
    width = cap.get(3)  # float
    height = cap.get(4)  # float
    fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (int(width), int(height)))
# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame

    ret, frame = cap.read()
    if ret == True:
        count = count + 1
        # Display the resulting frame
        # grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_copy = frame.copy()

        frame = frame_copy.copy()
        method = eval(methods[1])

        # Apply template Matching
        res1 = cv2.matchTemplate(frame, template1, method)



        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc1
        else:
            top_left = max_loc1
            bottom_right = (top_left[0] + 5, top_left[1] + 5)

        if max_val1 > 0.90:
            if flag == False:
                coins += 1
                flag = True
                frameno = 51

        if flag == True:
            if frameno:
                frameno = frameno - 1
            else:
                flag = False