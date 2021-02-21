img1=imread('p2_board_1.jpg');
img2=imread('p2_board_2.jpg');
img3=imread('p2_board_3.jpg');

black_on_white_pawn=imread('black_on_white_pawn.png');
black_on_black_pawn=imread('black_on_black_pawn.png');
white_on_black_pawn=imread('white_on_black_pawn.png');
white_on_white_pawn=imread('white_on_white_pawn.png');

img1=swapPawns(img1,black_on_white_pawn,black_on_black_pawn,...
                           white_on_black_pawn,white_on_white_pawn)
img2=swapPawns(img2,black_on_white_pawn,black_on_black_pawn,...
                           white_on_black_pawn,white_on_white_pawn)
img3=swapPawns(img3,black_on_white_pawn,black_on_black_pawn,...
                           white_on_black_pawn,white_on_white_pawn)
                       
imwrite(img1,'output/Part_2c/p2_board1.png');
imwrite(img2,'output/Part_2c/p2_board2.png');
imwrite(img3,'output/Part_2c/p2_board3.png');

figure();
imshow(img1);
figure();
imshow(img2);
figure();
imshow(img3);


function [img]= swapPawns(img,black_on_white_pawn,black_on_black_pawn,...
                           white_on_black_pawn,white_on_white_pawn)
                       
black_and_white_image=im2bw(img,0.55);
image_dup=img;
black_on_white_pawn_bw=im2bw(black_on_white_pawn);
white_on_white_pawn_bw=im2bw(white_on_black_pawn);
for i=1:60:421;
    for j=1:60:421;
        if sum(abs(black_and_white_image(i:i+59,j:j+59)-black_on_white_pawn_bw))<=5
            if sum(abs(image_dup(i:i+59,j:j+59)-black_on_white_pawn))< ...
                    sum(abs(image_dup(i:i+59,j:j+59)-black_on_black_pawn))
            img(i:i+59,j:j+59)=white_on_white_pawn;
            else
            img(i:i+59,j:j+59)=white_on_black_pawn;
            end    
        end
        
        if sum(abs(black_and_white_image(i:i+59,j:j+59)-white_on_white_pawn_bw))<=5
            diff = image_dup(i:i+59,j:j+59);
            r = sum((diff-white_on_black_pawn)); 
            t = sum((diff-white_on_white_pawn));   
            if t < r
            img(i:i+59,j:j+59)=black_on_white_pawn;
            else
            img(i:i+59,j:j+59)=black_on_black_pawn;
            end
        end
    end
end 
end
