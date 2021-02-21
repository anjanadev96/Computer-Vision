

#include <opencv2/opencv.hpp>
#include "opencv2/imgproc.hpp"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace cv;
using namespace std;

Scalar getMSSIM( const Mat& i1, const Mat& i2)
{
    const double C1 = 6.5025, C2 = 58.5225;
    
    int d     = CV_32F;

    Mat I1, I2;
    i1.convertTo(I1, d);         
    i2.convertTo(I2, d);

    Mat I2_2   = I2.mul(I2);        
    Mat I1_2   = I1.mul(I1);        
    Mat I1_I2  = I1.mul(I2);        


    Mat mu1, mu2;   
    GaussianBlur(I1, mu1, Size(11, 11), 1.5);
    GaussianBlur(I2, mu2, Size(11, 11), 1.5);

    Mat mu1_2   =   mu1.mul(mu1);
    Mat mu2_2   =   mu2.mul(mu2);
    Mat mu1_mu2 =   mu1.mul(mu2);

    Mat sigma1_2, sigma2_2, sigma12;

    GaussianBlur(I1_2, sigma1_2, Size(11, 11), 1.5);
    sigma1_2 -= mu1_2;

    GaussianBlur(I2_2, sigma2_2, Size(11, 11), 1.5);
    sigma2_2 -= mu2_2;

    GaussianBlur(I1_I2, sigma12, Size(11, 11), 1.5);
    sigma12 -= mu1_mu2;

    
    Mat t1, t2, t3;

    t1 = 2 * mu1_mu2 + C1;
    t2 = 2 * sigma12 + C2;
    t3 = t1.mul(t2);              

    t1 = mu1_2 + mu2_2 + C1;
    t2 = sigma1_2 + sigma2_2 + C2;
    t1 = t1.mul(t2);               

    Mat ssim_map;
    divide(t3, t1, ssim_map);      

    Scalar mssim = mean( ssim_map ); 
    return mssim;
}

Mat getLabels(const Mat &image,const Mat &black_on_black_pawn, const Mat &black_on_white_pawn, const Mat &white_on_black_pawn, const Mat &white_on_white_pawn)
 {  
    Scalar b_o_b_pawn;
    Scalar b_o_w_pawn;
    Scalar w_o_b_pawn;
    Scalar w_o_w_pawn;
    int number=1;

    for(int i=image.rows-60; i>0; i-=60)

    {

    for(int j=0; j<image.cols; j+=60)
     {  
        Rect roi(j,i,60,60);
        
        Mat cmp= image(roi);
        b_o_b_pawn= getMSSIM(cmp, black_on_black_pawn);
        b_o_w_pawn= getMSSIM(cmp, black_on_white_pawn);
        w_o_b_pawn= getMSSIM(cmp, white_on_black_pawn);
        w_o_w_pawn= getMSSIM(cmp, white_on_white_pawn); 

      if (b_o_b_pawn[0]>0.85 || b_o_w_pawn[0]>0.85 || w_o_b_pawn[0]>0.85 || w_o_w_pawn[0]>0.85) 
      {  string text=to_string(number);
        
          putText(image, text, Point(j+3,i+7), FONT_HERSHEY_COMPLEX_SMALL, 0.5, Scalar(0,0,0),1); 

          number++; 

         }


    }

}

return image;

}


int main(int argc, char** argv)
{
 // Read the image file
Mat image1 = imread("p2_board_1.jpg");
Mat image2 = imread("p2_board_2.jpg");
Mat image3 = imread("p2_board_3.jpg");

Mat black_on_black_pawn=imread("../../input/black_on_black_pawn.png");
Mat black_on_white_pawn=imread("../../input/black_on_white_pawn.png");
Mat white_on_white_pawn=imread("../../input/white_on_white_pawn.png");
Mat white_on_black_pawn=imread("../../input/white_on_black_pawn.png");

image1=getLabels(image1,black_on_black_pawn, black_on_white_pawn,white_on_black_pawn, white_on_white_pawn);
image2=getLabels(image2,black_on_black_pawn, black_on_white_pawn,white_on_black_pawn, white_on_white_pawn);
image3=getLabels(image3,black_on_black_pawn, black_on_white_pawn,white_on_black_pawn, white_on_white_pawn);




imwrite( "../../output/Part_2b/p2_board_1.png", image1);
imwrite( "../../output/Part_2b/p2_board_2.png", image2);
imwrite( "../../output/Part_2b/p2_board_3.png", image3);
 
 
 string windowName1 = "1";
 string windowName2 = "2";
 string windowName3 = "3"; //Name of the window

 namedWindow(windowName1); 
 namedWindow(windowName2);
 namedWindow(windowName3);// Create a window

 imshow(windowName1,image1);
 imshow(windowName2,image2);
 imshow(windowName3,image3); // Show our image inside the created window.

 waitKey(0); // Wait for any keystroke in the window

 destroyWindow(windowName1);
 waitKey(0); 
 destroyWindow(windowName2);
 waitKey(0); 
 destroyWindow(windowName3); //destroy the created window

 return 0;

}
