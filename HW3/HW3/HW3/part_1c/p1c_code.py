import cv2
import numpy as np


def NoOfLinesRemoved(input_file, output_file):

    hsv_yellow_l = np.array([30, 100, 100])
    hsv_yellow_u = np.array([50, 255, 255])

    hsv_green_l = np.array([50,100,100])
    hsv_green_u = np.array([70,255,255])

    hsv_blue_l =np.array([110,100,100])
    hsv_blue_u =np.array([130,255,255])

    hsv_cyan_l = np.array([80,100,100])
    hsv_cyan_u = np.array([100,255,255])

    hsv_orange_l = np.array([15,100,100])
    hsv_orange_u = np.array([25,255,255])

    hsv_red_l = np.array([0, 210,210])
    hsv_red_u = np.array([5, 255, 255])

    hsv_purple_l = np.array([140, 100, 100])
    hsv_purple_u = np.array([160, 255, 255])


    cap = cv2.VideoCapture(input_file)

    prev_count=0
    total_count=0
    lines_removed=0




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

            ans=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            thresh, ans_bw = cv2.threshold(ans, 128, 255, cv2.THRESH_BINARY)

            hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # cv2.imshow('HSVFrame', hsvframe)


            connectivity=8

            mask_cyan= cv2.inRange(hsvframe,hsv_cyan_l,hsv_cyan_u)
            mask_yellow = cv2.inRange(hsvframe, hsv_yellow_l, hsv_yellow_u)
            mask_green = cv2.inRange(hsvframe, hsv_green_l, hsv_green_u)
            mask_blue= cv2.inRange(hsvframe, hsv_blue_l, hsv_blue_u)
            mask_red = cv2.inRange(hsvframe, hsv_red_l, hsv_red_u)
            mask_orange= cv2.inRange(hsvframe, hsv_orange_l, hsv_orange_u)
            mask_purple=cv2.inRange(hsvframe, hsv_purple_l,hsv_purple_u)



            count_cyan, labels_1, stats_1, centroids_1=cv2.connectedComponentsWithStats(mask_cyan,connectivity)
            count_yellow, labels_2, stats_2, centroids_2 = cv2.connectedComponentsWithStats(mask_yellow, connectivity)
            count_green, labels_3, stats_3, centroids_3 = cv2.connectedComponentsWithStats(mask_green, connectivity)
            count_blue, labels_4, stats_4, centroids_4 = cv2.connectedComponentsWithStats(mask_blue, connectivity)
            count_red, labels_5, stats_5, centroids_5 = cv2.connectedComponentsWithStats( mask_red, connectivity)
            count_orange, labels_6, stats_6, centroids_6 = cv2.connectedComponentsWithStats(mask_orange, connectivity)
            count_purple, labels_7, stats_7, centroids_7 = cv2.connectedComponentsWithStats(mask_purple, connectivity)

            count_cyan=sum(stats_1[:,4]>3000)
            count_yellow=sum(stats_2[:,4]>3000)
            count_green=sum(stats_3[:,4]>3000)
            count_blue=sum(stats_4[:,4]>3000)
            count_red= sum(stats_5[:,4]>3000)
            count_orange=sum(stats_6[:,4]>3000)
            count_purple=sum(stats_7[:,4]>3000)

            count_cyan=count_cyan-1
            count_yellow=count_yellow-1
            count_green=count_green-1
            count_blue=count_blue-1
            count_red=count_red-1
            count_orange=count_orange-1
            count_purple=count_purple-1

            total_count = count_cyan + count_yellow + count_green + count_red + count_blue + count_orange + count_purple
            diff = total_count - prev_count
            if diff<-6:
                lines_removed+=1
            if diff<-10:
                lines_removed+=1



            str1="Lines Removed : " +str(lines_removed)
            print(str1)

            cv2.putText(frame,str1,(20, 50),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255),2,cv2.LINE_AA)
         

            prev_count=total_count

            out.write(frame)


            cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
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





#NoOfLinesRemoved('p1c_tetris_1.mp4','p1c_tetris_1_output.avi')
NoOfLinesRemoved('p1c_tetris_2.mp4', 'p1c_tetris_2_output.avi')



