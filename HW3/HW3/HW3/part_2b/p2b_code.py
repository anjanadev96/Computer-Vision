import cv2
import numpy as np
from skimage.metrics import structural_similarity

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
def compareImages(img1,img2):
    sim=structural_similarity(img1,img2)
    print(sim)
    if sim>0.20:
        return True
    return False


def CountCoins(input_file, output_file):
    count=0
    coins=0
    coins_on_screen=0
    coins_left=0
    flag=False
    enter=False
    frameno=0
    prev_frame=0
    cap = cv2.VideoCapture(input_file)
    blue_sky_coin=cv2.imread("coin4.png")
    coin_dark = cv2.imread("Darkcoin.png")
    coin_light=cv2.imread("Lightcoin.png")
    


    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    prev_max_val1=0
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
            count = count + 1
            # Display the resulting frame
            #grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_copy=frame.copy()


            frame = frame_copy.copy()
            method = eval(methods[1])

            # Apply template Matching
            res1 = cv2.matchTemplate(frame, blue_sky_coin, method)
            min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)


            if max_val1>0.90:
                if flag==False:
                    coins+=1
                    flag=True
                    frameno=51

            if flag==True:
                if frameno:
                    frameno=frameno-1
                else:
                    flag=False


            else:
                if frameno:
                    frameno=frameno-1
                else:
                    flag=False

            if count != 1:
                 prev_frame_bw = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
                 curr_frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                 ans = compareImages(prev_frame_bw, curr_frame_bw)

                 if ans == False:
                    if enter==False:
                         res2 = cv2.matchTemplate(frame, coin_light, method)


                         loc = np.where(res2 >= 0.98)
                         for pt in zip(*loc[::-1]):
                             coins_on_screen += 1
                         print("Coins_on_screen", coins_on_screen)
                         enter=True
                         ans=True
                    else:
                        res3 = cv2.matchTemplate(prev_frame, coin_dark, method)
                        loc = np.where(res3 >= 0.98)
                        for pt in zip(*loc[::-1]):
                            coins_left += 1
                        coins += coins_on_screen - coins_left
                        print("Coins left", coins_left)
            #



            print(max_val1, "    ", coins)

            str1 = "Coins Collected: " + str(coins)


            cv2.putText(frame, str1, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
            out.write(frame)
            cv2.imshow("Frame",frame)

            prev_frame=frame


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



#CountCoins('p2b_mario_1.mp4','p2b_mario_1_output.avi')
CountCoins('p2b_mario_2.mp4','p2b_mario_2_output.avi')
#CountCoins('p2b_mario_3.mp4','p2b_mario_3_output.avi')

