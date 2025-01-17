#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
 // Read the image file
 Mat image = imread("p1_board.jpg",0);

 // Check for failure
 if (image.empty()) 
 {
  cout << "Could not open or find the image" << endl;
  cin.get(); //wait for any key press
  return -1;
 }

 String windowName = "1"; //Name of the window

 namedWindow(windowName); // Create a window
 cout<<image.rows;
 cout<<image.cols;
 image=400-image;
 imwrite("../../output/Part_1b/part_1b_cv.png",image);
 imshow(windowName, image); // Show our image inside the created window.

 waitKey(0); // Wait for any keystroke in the window

 destroyWindow(windowName); //destroy the created window

 return 0;
}
