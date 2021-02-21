import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name


def FindMario(input_file, output_file):

    cap = cv2.VideoCapture(input_file)
    template1=cv2.imread("Big_Mario_fleft.png",0)
    template2=cv2.imread("Big_Mario_fright.png",0)
    template3 = cv2.imread("Small_Mario_fleft.png", 0)
    template4 = cv2.imread("Small_Mario_fright.png", 0)

    w1, h1 = template1.shape[::-1]
    w2, h2 = template2.shape[::-1]
    w3, h3 = template3.shape[::-1]
    w4, h4 = template4.shape[::-1]

    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']


    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video stream or file")

    if cap.isOpened():
        width = cap.get(3)  # float
        height = cap.get(4)  # float
        fps= cap.get(cv2.CAP_PROP_FPS)



    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, fps, (int(width), int(height)))
    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame

        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame
            grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            grayFrame_copy=grayFrame.copy()


            grayFrame = grayFrame_copy.copy()
            method = eval(methods[3])

            # Apply template Matching
            res1 = cv2.matchTemplate(grayFrame, template1, method)
            res2 = cv2.matchTemplate(grayFrame, template2, method)
            res3 = cv2.matchTemplate(grayFrame, template3, method)
            res4 = cv2.matchTemplate(grayFrame, template4, method)

            min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)
            min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)
            min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(res3)
            min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(res4)

            min_val=min(min_val1,min_val2,min_val3,min_val4)
            max_val=max(max_val1,max_val2,max_val3,max_val4)
            if min_val==min_val1:
                min_loc=min_loc1
                w,h=w1,h1
            if min_val==min_val2:
                min_loc=min_loc2
                w,h=w2,h2
            if min_val==min_val3:
                min_loc=min_loc3
                w,h=w3,h3
            if min_val==min_val4:
                min_loc=min_loc4
                w,h=w4,h4
            if max_val==max_val1:
                max_loc=max_loc1
                w,h=w1,h1
            if max_val==max_val2:
                max_loc=max_loc2
                w,h=w2,h2
            if max_val==max_val3:
                max_loc=max_loc3
                w,h=w3,h3
            if max_val==max_val4:
                max_loc=max_loc4
                w,h=w4,h4


            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            cv2.rectangle(frame, top_left, bottom_right, 255, 2)

            out.write(frame)
            cv2.imshow("Frame",frame)


            # Press Q on keyboard to  exit
            if cv2.waitKey(25) == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()



#FindMario('p2a_mario_1.mp4','p2a_mario_1_output.avi')
#FindMario('p2a_mario_2.mp4', 'p2a_mario_2_output.avi')
FindMario('p2a_mario_3.mp4','p2a_mario_3_output.avi')
