import cv2

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name


def ConvertRGBtoGrayScale(input_file, output_file):

    cap = cv2.VideoCapture(input_file)



    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video stream or file")

    if cap.isOpened():
        width = cap.get(3)  # float
        height = cap.get(4)  # float
        fps= cap.get(cv2.CAP_PROP_FPS)



    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, fps, (int(width), int(height)),False)
    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame

        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame

            grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('grayFrame', grayFrame)
            out.write(grayFrame)

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



ConvertRGBtoGrayScale('p1a_tetris_1.mp4','p1a_tetris_1_output.avi')
ConvertRGBtoGrayScale('p1a_tetris_2.mp4', 'p1a_tetris_2_output.avi')
