img=imread('p2_board_3.jpg');
figure;
imshow(img);
img1=img;
black_on_white_pawn=imread('black_on_white_pawn.png');
black_on_black_pawn=imread('black_on_black_pawn.png');
white_on_black_pawn=imread('white_on_black_pawn.png');
white_on_white_pawn=imread('white_on_white_pawn.png');

black_on_white_pawn1=imread('black_on_white_pawn.png');
black_on_black_pawn1=imread('black_on_black_pawn.png');
white_on_black_pawn1=imread('white_on_black_pawn.png');
white_on_white_pawn1=imread('white_on_white_pawn.png');






for i=1:60:421;
    for j=1:60:421;
        if sum(abs(img1(i:i+59,j:j+59)-black_on_white_pawn1))<=10
            img(i:i+59,j:j+59)=white_on_white_pawn;
        end
        if sum(abs(img1(i:i+59,j:j+59)-black_on_black_pawn1))<=100
            img(i:i+59,j:j+59)=white_on_black_pawn;
        end
        if sum(abs(img1(i:i+59,j:j+59)-white_on_black_pawn1))<=10
            img(i:i+59,j:j+59)=black_on_black_pawn;
        end
        if sum(abs(img1(i:i+59,j:j+59)-white_on_white_pawn1))<=100
            img(i:i+59,j:j+59)=black_on_white_pawn;
        end
    end
end 
figure;
imshow(img);