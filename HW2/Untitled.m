img=imread('input/Part_4/p4_board_3.jpg');
gray_img=rgb2gray(img);
imshow(gray_img);
black_and_white_image=im2bw(gray_img,0.55);
image_dup=gray_img;
figure;
imshow(image_dup);

black_on_white_queen=gray_img(121:180,121:180);
imwrite(black_on_white_queen,'programs/black_on_white_queen.png');

black_on_white_pawn=imread('black_on_white_pawn.png');
black_on_black_pawn=imread('black_on_black_pawn.png');
white_on_black_pawn=imread('white_on_black_pawn.png');
white_on_white_pawn=imread('white_on_white_pawn.png');

black_on_white_queen=imread('black_on_white_queen.png');
black_on_black_queen=imread('black_on_black_queen.png');
white_on_black_queen=imread('white_on_black_queen.png');
white_on_white_queen=imread('white_on_white_queen.png');

ssimval=ssim(black_on_white_queen,black_on_black_queen)
disp(ssimval)

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
figure;
imshow(gray_img);
