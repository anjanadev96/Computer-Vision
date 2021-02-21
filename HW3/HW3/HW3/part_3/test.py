import cv2

cap = cv2.VideoCapture('p3_tetris_1.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

if cap.isOpened():
    width = cap.get(3)  # float
    height = cap.get(4)  # float
    fps = cap.get(cv2.CAP_PROP_FPS)