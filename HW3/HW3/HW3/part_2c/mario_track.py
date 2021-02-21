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

def FindMario(input,i):

    ignore = False
    global count
    global ignore_counter
    ignore_counter = ignore_counter - 1
    frame=cv2.imread(input)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 180, 180])
    upper_red = np.array([4, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    img2 = hsv
    ans = cv2.bitwise_and(img2, img2, mask=mask)
    template = cv2.imread('mario_mush.png')
    template1= cv2.imread('fireball1.png')
    #res, max_val, max_loc, w, h = Mario_Match(template, frame)

    bluecnts = cv2.findContours(mask.copy(),
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(bluecnts) > 0:
        blue_area = max(bluecnts, key=cv2.contourArea)
        (xg, yg, wg, hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(ans, (xg-25, yg+10), (xg + wg+75, yg + hg+90), (0, 255, 0), 2)

        # cv2.rectangle(frame, (xg, yg), (xg + wg, yg + hg), (0, 255, 0), 2)
        cv2.imshow("frame", frame)
        cv2.imshow("mask",ans)
        cv2.waitKey(10)
        #print(max_val)

        # top_left = max_loc
        # bottom_right = (top_left[0] + 45, top_left[1] + 100)
        # cv2.rectangle(frame, top_left, bottom_right, 255, 2)
        # roi = [[top_left[0], top_left[1]], [top_left[0]+45,top_left[1]], [top_left[0], top_left[1]+85], [bottom_right]]
        roi = frame[yg+10:yg+hg+90, xg-25:xg+wg+75]
        #print(roi)

        res,max_val,max_loc,w,h=Mario_Match(template1,roi)
        if ignore_counter>0:
            ignore = True
        if max_val>0.85 and ignore==False:
            count = count +1
            print(max_val,i)
            ignore = True
            ignore_counter = 10
        cv2.imshow("roi",roi)

        cv2.imshow("frame", ans)
        cv2.imshow("frame2", frame)










for i in range(3300,3510):
    file = "frames/" + str(i) + ".png"
    print(i)
    FindMario(file,i)
# FindMario("frames/3509.png",3509)
print(count)