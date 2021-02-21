img1=imread('input/Part_4/p4_board_1.jpg');
img2=imread('input/Part_4/p4_board_2.jpg');
img3=imread('input/Part_4/p4_board_3.jpg');


black_on_white_pawn=imread('black_on_white_pawn.png');
black_on_black_pawn=imread('black_on_black_pawn.png');
white_on_black_pawn=imread('white_on_black_pawn.png');
white_on_white_pawn=imread('white_on_white_pawn.png');

black_on_white_queen=imread('black_on_white_queen.png');
black_on_black_queen=imread('black_on_black_queen.png');
white_on_black_queen=imread('white_on_black_queen.png');
white_on_white_queen=imread('white_on_white_queen.png');

img1= ReplaceWithQueens(img1,black_on_white_pawn,black_on_black_pawn,...
                                  white_on_black_pawn,white_on_white_pawn,...
                                  black_on_white_queen,black_on_black_queen,...
                                  white_on_black_queen,white_on_white_queen)
img2= ReplaceWithQueens(img2,black_on_white_pawn,black_on_black_pawn,...
                                  white_on_black_pawn,white_on_white_pawn,...
                                  black_on_white_queen,black_on_black_queen,...
                                  white_on_black_queen,white_on_white_queen)
img3= ReplaceWithQueens(img3,black_on_white_pawn,black_on_black_pawn,...
                                  white_on_black_pawn,white_on_white_pawn,...
                                  black_on_white_queen,black_on_black_queen,...
                                  white_on_black_queen,white_on_white_queen)
                              
imwrite(img1,'output/Part_4b/p4_board1.png');
imwrite(img2,'output/Part_4b/p4_board2.png');
imwrite(img3,'output/Part_4b/p4_board3.png');

figure();
imshow(img1);
figure();
imshow(img2);
figure();
imshow(img3);





function [gray_img]= ReplaceWithQueens(img,black_on_white_pawn,black_on_black_pawn,...
                                  white_on_black_pawn,white_on_white_pawn,...
                                  black_on_white_queen,black_on_black_queen,...
                                  white_on_black_queen,white_on_white_queen)
gray_img=rgb2gray(img);
gray_img=medfilt2(gray_img)
black_and_white_image=im2bw(gray_img,0.55);
image_dup=gray_img;
black_on_white_pawn_bw=im2bw(black_on_white_pawn);
white_on_white_pawn_bw=im2bw(white_on_black_pawn);

for i=1:420:421;
    for j=1:60:421;
        
        a1=ssim(image_dup(i:i+59,j:j+59),black_on_white_pawn)
        a2=ssim(image_dup(i:i+59,j:j+59),black_on_black_pawn)
        a3=ssim(image_dup(i:i+59,j:j+59),white_on_white_pawn)
        a4=ssim(image_dup(i:i+59,j:j+59),white_on_black_pawn)
       if sum(abs(black_and_white_image(i:i+59,j:j+59)-white_on_white_pawn_bw))<=5 
            if a3>0.95
            gray_img(i:i+59,j:j+59)=white_on_white_queen;
            else
            gray_img(i:i+59,j:j+59)=white_on_black_queen;
            end  
       end
        
       if sum(abs(black_and_white_image(i:i+59,j:j+59)-black_on_white_pawn_bw))<=5 
            if a1>0.90
                gray_img(i:i+59,j:j+59)=black_on_white_queen;
            else
                gray_img(i:i+59,j:j+59)=black_on_black_queen;
            end
       end
        
    end
end 

end
