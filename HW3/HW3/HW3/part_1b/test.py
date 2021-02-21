import cv2
import numpy as np
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name


def CounterForSquares(input_file, output_file):

    hsv_yellow_l = np.array([30, 100, 100])
    hsv_yellow_u = np.array([50, 255, 255])

    hsv_green_l = np.array([50,100,100])
    hsv_green_u = np.array([70,255,255])

    hsv_blue_l =np.array([110,100,100])
    hsv_blue_u =np.array([130,255,255])

    hsv_cyan_l = np.array([80,100,100])
    hsv_cyan_u = np.array([100,255,255])

    hsv_orange_l = np.array([10,100,100])
    hsv_orange_u = np.array([30,255,255])

    hsv_red_l = np.array([0, 100, 100])
    hsv_red_u = np.array([10, 255, 255])

    hsv_purple_l = np.array([140, 100, 100])
    hsv_purple_u = np.array([160, 255, 255])


    cap = cv2.VideoCapture(input_file)



    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video stream or file")

    if cap.isOpened():
        width = cap.get(3)  # float
        height = cap.get(4)  # float
        fps= cap.get(cv2.CAP_PROP_FPS)



    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter(output_file, fourcc, fps, (int(width), int(height)),False)
    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame


        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame


            hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imshow('HSVFrame', hsvframe)




            mask_cyan= cv2.inRange(hsvframe,hsv_cyan_l,hsv_cyan_u)
            mask_yellow = cv2.inRange(hsvframe, hsv_yellow_l, hsv_yellow_u)
            mask_green = cv2.inRange(hsvframe, hsv_green_l, hsv_green_u)
            mask_blue= cv2.inRange(hsvframe, hsv_blue_l, hsv_blue_u)
            mask_red = cv2.inRange(hsvframe, hsv_red_l, hsv_red_u)
            mask_orange= cv2.inRange(hsvframe, hsv_orange_l, hsv_orange_u)
            mask_purple=cv2.inRange(hsvframe, hsv_purple_l,hsv_purple_u)

            ret, markers=cv2.connectedComponents(mask_orange)
            print(markers)




            #res=cv2.bitwise_and(frame,frame, mask=mask)

            cv2.imshow('Frame',frame)
            cv2.imshow('Mask',mask_red)
            cv2.imshow('Mask1', mask_orange)

            #cv2.imshow('Res',res)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) == ord('q'):
                break

        # Break the loop
        else:
            break


    # When everything done, release the video capture object
    cap.release()
    #out.release()

    # Closes all the frames
    cv2.destroyAllWindows()



CounterForSquares('p1b_tetris_1.mp4','p1b_tetris_1_output.avi')
#CounterForSquares('p1b_tetris_2.mp4', 'p1b_tetris_2_output.avi')



