import cv2
import numpy as np
import math

ignore_counter = 0
ignore = False
count  = 0
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def Mario_Match(template, img2):
    # w, h = template.shape[::-1]

    w,h = 5, 5
    # All the 6 methods for comparison in a list
    img = img2.copy()
    method = eval('cv2.TM_CCOEFF_NORMED')
    # Apply template Mario_Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return res,max_val, max_loc,w,h

def FindMario(input_file,i, output_file,ln):
    cap = cv2.VideoCapture(input_file)
    coins = 0
    coins_on_screen = 0
    coins_left = 0
    flag = False
    enter = False
    prev_frame = 0
    frameno = 0
    template2 = cv2.imread("coin2.png")
    template3 = cv2.imread("coinblack.png")


    global count
    global ignore_counter

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
        ignore_counter = ignore_counter - 1
        ignore = False

        if ret == True:
            # Display the resulting frame
            # grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_copy = frame.copy()
            i=i+1
            print(i)
            frame = frame_copy.copy()
            res1,max_val1,max_loc1,w1,h1 = Mario_Match(frame, template2)
            res2,max_val2,max_loc2,w2,h2= Mario_Match(frame, template3)



            if max_val1 > 0.90 and max_val1>max_val2:
                if flag == False:
                    coins += 1
                    flag = True
                    frameno = 60

            if flag == True:
                if frameno:
                    frameno = frameno - 1
                else:
                    flag = False


            else:
                if frameno:
                    frameno = frameno - 1
                else:
                    flag = False

            if max_val2 > 0.80 and max_val2 > max_val1:
                if flag == False:
                    coins += 1
                    flag = True
                    frameno = 75

            if flag == True:
                if frameno:
                    frameno = frameno - 1
                else:
                    flag = False


            else:
                if frameno:
                    frameno = frameno - 1
                else:
                    flag = False



            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_red = np.array([0, 180, 180])
            upper_red = np.array([4, 255, 255])
            mask = cv2.inRange(hsv, lower_red, upper_red)
            img2 = hsv
            ans = cv2.bitwise_and(img2, img2, mask=mask)
            template = cv2.imread('mario_mush.png')
            template1= cv2.imread('fireball1.png')

            bluecnts = cv2.findContours(mask.copy(),
                                        cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)[-2]

            if len(bluecnts) > 0:
                blue_area = max(bluecnts, key=cv2.contourArea)
                (xg, yg, wg, hg) = cv2.boundingRect(blue_area)
                cv2.rectangle(ans, (xg-25, yg+10), (xg + wg+75, yg + hg+90), (0, 255, 0), 2)

                frame_height = frame.shape[1]
                frame_width = frame.shape[0]


                if i<ln:
                    roi = frame[yg + 10:yg + hg + 90, xg - 25:xg + wg + 75]


                    res,max_val,max_loc,w,h=Mario_Match(template1,roi)
                    if ignore_counter>0:
                        ignore = True
                    if max_val>0.85 and ignore==False:
                        count = count +1
                        print(max_val,i, count)
                        ignore = True
                        ignore_counter = 7
                    cv2.imshow("roi",roi)
                cv2.imshow("frame", ans)
                    # out.write(frame)
                cv2.waitKey(10)

            str1 = "Coins Collected: " + str(coins)

            cv2.putText(frame, str1, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            projectile_count = "Projectiles Fired: " + str(count)

            cv2.putText(frame, projectile_count, (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            out.write(frame)
            cv2.imshow("mario frame", frame)

            if cv2.waitKey(25) == ord('q'):
                break
            # Break the loop
        else:
            break

            # When everything done, release the video capture object
    cap.release()
    out.release()

    cv2.destroyAllWindows()





FindMario("p2c_mario_1.mp4",0, "p2c_mario_1_output.avi", 3065)
#FindMario("p2c_mario_2.mp4",0, "p2c_mario_2_output.avi", 2034)
