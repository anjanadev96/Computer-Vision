img1=imread('input/Part_6/p6_board_1.jpg');
img2=imread('input/Part_6/p6_board_2.jpg');
img3=imread('input/Part_6/p6_board_3.jpg');

black_on_black_queen=imread('black_on_black_queen.png');
black_on_white_queen=imread('black_on_white_queen.png');
white_on_black_queen=imread('white_on_black_queen.png');
white_on_white_queen=imread('white_on_white_queen.png');

black_on_white_pawn=imread('black_on_white_pawn.png');
black_on_black_pawn=imread('black_on_black_pawn.png');
white_on_black_pawn=imread('white_on_black_pawn.png');
white_on_white_pawn=imread('white_on_white_pawn.png');


img1=SwapPawnsAndQueens(img1,black_on_black_queen, black_on_white_queen, ...
                                   white_on_black_queen,white_on_white_queen,...
                                   black_on_white_pawn,black_on_black_pawn,...
                                   white_on_black_pawn,white_on_white_pawn)
                               
img2=SwapPawnsAndQueens(img2,black_on_black_queen, black_on_white_queen, ...
                                   white_on_black_queen,white_on_white_queen,...
                                   black_on_white_pawn,black_on_black_pawn,...
                                   white_on_black_pawn,white_on_white_pawn)
                               
img3=SwapPawnsAndQueens(img3,black_on_black_queen, black_on_white_queen, ...
                                   white_on_black_queen,white_on_white_queen,...
                                   black_on_white_pawn,black_on_black_pawn,...
                                   white_on_black_pawn,white_on_white_pawn)
                               
imwrite(img1,'output/Part_6a/p6_board1.png');
imwrite(img2,'output/Part_6a/p6_board2.png');
imwrite(img3,'output/Part_6a/p6_board3.png');                              
                               
                               
figure();
imshow(img1);
figure();
imshow(img2);
figure();
imshow(img3);





function [img]=SwapPawnsAndQueens(img,black_on_black_queen, black_on_white_queen, ...
                                   white_on_black_queen,white_on_white_queen,...
                                   black_on_white_pawn,black_on_black_pawn,...
                                   white_on_black_pawn,white_on_white_pawn)

img=rgb2gray(img);


for i=1:60:421;
    for j=1:60:421;
        
        if ssim(img(i:i+59,j:j+59),black_on_black_pawn)>0.95
            img(i:i+59,j:j+59)= black_on_black_queen;
        elseif ssim(img(i:i+59,j:j+59),black_on_white_pawn)>0.95
            img(i:i+59,j:j+59)= black_on_white_queen;
        elseif ssim(img(i:i+59,j:j+59),white_on_black_pawn)>0.95
            img(i:i+59,j:j+59)= white_on_black_queen;
        
        elseif ssim(img(i:i+59,j:j+59),white_on_white_pawn)>0.95
            img(i:i+59,j:j+59)= white_on_white_queen;
        elseif ssim(img(i:i+59,j:j+59),black_on_black_queen)>0.95
            img(i:i+59,j:j+59)= black_on_black_pawn;
        elseif ssim(img(i:i+59,j:j+59),black_on_white_queen)>0.95
            img(i:i+59,j:j+59)= black_on_white_pawn;
        elseif ssim(img(i:i+59,j:j+59),white_on_black_queen)>0.95
            img(i:i+59,j:j+59)= white_on_black_pawn;
        
        elseif ssim(img(i:i+59,j:j+59),white_on_white_queen)>0.95
            img(i:i+59,j:j+59)= white_on_white_pawn;
        end
            
    end
end

end
            
                
        
            
            
        
                                   

                                   

