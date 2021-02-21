

#include <opencv2/opencv.hpp>
#include "opencv2/imgproc.hpp"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace cv;
using namespace std;

 Mat black_on_black_pawn;
 Mat black_on_white_pawn;
 Mat white_on_white_pawn;
 Mat white_on_black_pawn;

 Mat black_on_black_bishop;
 Mat black_on_white_bishop;
 Mat white_on_white_bishop;
 Mat white_on_black_bishop;

 Mat black_on_black_knight;
 Mat black_on_white_knight;
 Mat white_on_white_knight;
 Mat white_on_black_knight;

 Mat black_on_black_rook;
 Mat black_on_white_rook;
 Mat white_on_white_rook;
 Mat white_on_black_rook;

 Mat black_on_black_queen;
 Mat black_on_white_queen;
 Mat white_on_white_queen;
 Mat white_on_black_queen;

 Mat black_on_black_king;
 Mat black_on_white_king;
 Mat white_on_white_king;
 Mat white_on_black_king;

 Mat black_square;
 Mat white_square;




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

string detectChessPiece(const Mat &image)
 
 {  string ans;
     
    Scalar b_pawn;
    Scalar w_pawn;
    

    Scalar b_rook;
    Scalar w_rook;

    Scalar b_knight;
    Scalar w_knight;

    Scalar b_bishop;
    Scalar w_bishop;

    Scalar b_queen;
    Scalar w_queen;

    Scalar b_king;
    Scalar w_king;

    Scalar b;
    Scalar w;


    
    b_pawn=getMSSIM(black_on_black_pawn,image);
    w_pawn=getMSSIM(white_on_white_pawn,image);

    b_rook=getMSSIM(black_on_black_rook,image);
    w_rook=getMSSIM(white_on_white_rook,image);

    b_knight=getMSSIM(black_on_black_knight,image);
    w_knight=getMSSIM(white_on_white_knight,image);

    b_bishop=getMSSIM(black_on_black_bishop,image);
    w_bishop=getMSSIM(white_on_white_bishop,image);

    b_queen=getMSSIM(black_on_black_queen,image);
    w_queen=getMSSIM(white_on_white_queen,image);

    

    b_king=getMSSIM(black_on_white_king,image);
    w_king=getMSSIM(white_on_black_king,image);

    b=getMSSIM(black_square,image);
    w=getMSSIM(white_square,image);


    if(b_pawn[0]>0.85)
        ans="Black Pawn";
    else if(w_pawn[0]>0.85)
        ans="White Pawn";
    else if(b_rook[0]>0.85)
        ans="Black Rook";
    else if(w_rook[0]>0.85)
        ans="White Rook";
    else if(b_knight[0]>0.85)
        ans="Black Knight";
    else if(w_knight[0]>0.85)
        ans="White Knight";
    else if(b_bishop[0]>0.85)
        ans="Black Bishop";
    else if(w_bishop[0]>0.85)
        ans="White Bishop";
    else if(b_queen[0]>0.85)
        ans="Black Queen";
    else if(w_queen[0]>0.85)
        ans="White Queen";
    else if(b_king[0]>0.85)
        ans="Black King";
    else if(w_king[0]>0.85)
        ans="White King";
    else 
        ans="Empty";

    return ans;

 }

void WriteToFile(string imagename, string filename)
{ 
   Mat unfiltered_img=imread(imagename); 
   Mat img;
   medianBlur(unfiltered_img,img,3);

   ofstream myfile;
   myfile.open(filename);
   
    char number='8';


 for(int i=0; i<img.rows; i+=60)

{  char letter='A';
 
  for(int j=0; j<img.cols; j+=60)
      
      {   
        string ans;
        
        Rect roi(j,i,60,60);
        
        // Mat cmp= image(roi);
        Mat cmp= img(roi);

        ans.push_back(letter);
        ans.push_back(number);
        ans+=" : ";
        ans+=detectChessPiece(cmp);
        ans+="\n";
        myfile<<ans;
        
        letter++;

     }
        cout<<endl;
        number--;

 }


myfile.close();
      


}
    




int main(int argc, char** argv)
{
 // Read the image file
string imagename1= "p5_board_1b_grain.jpg";
string imagename2= "p5_board_2b_grain.jpg";
string imagename3= "p5_board_3b_grain.jpg";

string filename1="5b_ans1.txt";
string filename2="5b_ans2.txt";
string filename3="5b_ans3.txt";


black_on_black_pawn=imread("../../input/black_on_black_pawn.png");
black_on_white_pawn=imread("../../input/black_on_white_pawn.png");
white_on_white_pawn=imread("../../input/white_on_white_pawn.png");
white_on_black_pawn=imread("../../input/white_on_black_pawn.png");

black_on_black_bishop=imread("../../input/black_on_black_bishop.png");
black_on_white_bishop=imread("../../input/black_on_white_bishop.png");
white_on_white_bishop=imread("../../input/white_on_white_bishop.png");
white_on_black_bishop=imread("../../input/white_on_black_bishop.png");

black_on_black_rook=imread("../../input/black_on_black_rook.png");
black_on_white_rook=imread("../../input/black_on_white_rook.png");
white_on_white_rook=imread("../../input/white_on_white_rook.png");
white_on_black_rook=imread("../../input/white_on_black_rook.png");

black_on_black_queen=imread("../../input/black_on_black_queen.png");
black_on_white_queen=imread("../../input/black_on_white_queen.png");
white_on_white_queen=imread("../../input/white_on_white_queen.png");
white_on_black_queen=imread("../../input/white_on_black_queen.png");

black_on_black_knight=imread("../../input/black_on_black_knight.png");
black_on_white_knight=imread("../../input/black_on_white_knight.png");
white_on_white_knight=imread("../../input/white_on_white_knight.png");
white_on_black_knight=imread("../../input/white_on_black_knight.png");

black_on_black_king=imread("../../input/black_on_black_king.png");
black_on_white_king=imread("../../input/black_on_white_king.png");
white_on_white_king=imread("../../input/white_on_white_king.png");
white_on_black_king=imread("../../input/white_on_black_king.png");

black_square=imread("../../input/black_square.png");
white_square=imread("../../input/white_square.png");

WriteToFile(imagename1,filename1);
WriteToFile(imagename2,filename2);
WriteToFile(imagename3,filename3);
    


 return 0;

}
