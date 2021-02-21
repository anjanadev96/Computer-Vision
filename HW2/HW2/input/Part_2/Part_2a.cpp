

#include <opencv2/opencv.hpp>

#include "opencv2/imgproc.hpp"
#include <iostream>
#include <string>
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


void fun(string input, string output)
{
 // Read the image file
Mat image = imread(input);

Mat black_on_black_pawn=imread("../../input/black_on_black_pawn.png");
Mat black_on_white_pawn=imread("../../input/black_on_white_pawn.png");
Mat white_on_white_pawn=imread("../../input/white_on_white_pawn.png");
Mat white_on_black_pawn=imread("../../input/white_on_black_pawn.png");

Scalar b_o_b_pawn;
Scalar b_o_w_pawn;
Scalar w_o_b_pawn;
Scalar w_o_w_pawn;

cout<<image.rows<<endl;
cout<<image.cols<<endl;
int count  = 0;





	for(int i=0; i<image.rows; i+=60)

	{

	for(int j=0; j<image.cols; j+=60)
	 {Rect roi(j,i,60,60);
		count++;
	  Mat cmp= image(roi);
	  b_o_b_pawn= getMSSIM(cmp, black_on_black_pawn);
	  b_o_w_pawn= getMSSIM(cmp, black_on_white_pawn);
	  w_o_b_pawn= getMSSIM(cmp, white_on_black_pawn);
	  w_o_w_pawn= getMSSIM(cmp, white_on_white_pawn); 
	  if (b_o_b_pawn[0]>0.95)
	  {Rect r=Rect(j,i,58,58);
	  rectangle(image,r,Scalar(255,0,0),2,8,0);}
	  if (b_o_w_pawn[0]>0.95)
	  {Rect r=Rect(j,i,58,58);
	  rectangle(image,r,Scalar(255,0,0),2,8,0);}
	  if (w_o_b_pawn[0]>0.95)
      {Rect r=Rect(j,i,58,58);
	  rectangle(image,r,Scalar(255,0,0),2,8,0);}
	  if (w_o_w_pawn[0]>0.95)
	  {Rect r=Rect(j,i,58,58);
	  rectangle(image,r,Scalar(255,0,0),2,8,0);}


	}

}

	

	

cout<<count<<endl;
imwrite( output, image);
 
 
 string windowName = "1"; //Name of the window

 namedWindow(windowName); // Create a window

 imshow(windowName,image); // Show our image inside the created window.

 waitKey(0); // Wait for any keystroke in the window

 destroyWindow(windowName); //destroy the created window

 return ;
}


int main(){
    fun("p2_board_1.jpg","../../output/Part_2a/2a1.png");
    fun("p2_board_2.jpg","../../output/Part_2a/2a2.png");
    fun("p2_board_3.jpg","../../output/Part_2a/2a3.png");

    return 0;
}