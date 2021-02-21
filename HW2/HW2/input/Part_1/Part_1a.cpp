

#include <opencv2/opencv.hpp>

#include "opencv2/imgproc.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
 // Read the image file
 Mat image = imread("p1_board.jpg");

char letter='a'; // Starting letter
char number='8'; // Starting number

for(int i=0; i<image.rows; i+=60)

{char number='8';

for(int j=0; j<image.cols; j+=60)
{
string text;
text.push_back(letter);
text.push_back(number);
putText(image, text, Point(i+30,j+30), FONT_HERSHEY_COMPLEX_SMALL, 0.7, Scalar(0,0,0), 1);

number--;}

letter++;}

imwrite( "../../output/Part_1a/Part_1a.png", image);
 
 
 String windowName = "1"; //Name of the window

 namedWindow(windowName); // Create a window

 imshow(windowName,image); // Show our image inside the created window.

 waitKey(0); // Wait for any keystroke in the window

 destroyWindow(windowName); //destroy the created window

 return 0;
}
