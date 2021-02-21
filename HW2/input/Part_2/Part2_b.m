img1=imread('p2_board_1.jpg');
img2=imread('p2_board_2.jpg');
img3=imread('p2_board_3.jpg');
count=0
black_on_white_pawn=imread('black_on_white_pawn.png');
black_on_black_pawn=imread('black_on_black_pawn.png');
white_on_black_pawn=imread('white_on_black_pawn.png');
white_on_white_pawn=imread('white_on_white_pawn.png');

img1=countPawns(img1,black_on_white_pawn,black_on_black_pawn,white_on_black_pawn,white_on_white_pawn,count)
img2=countPawns(img2,black_on_white_pawn,black_on_black_pawn,white_on_black_pawn,white_on_white_pawn,count)
img3=countPawns(img3,black_on_white_pawn,black_on_black_pawn,white_on_black_pawn,white_on_white_pawn,count)

imwrite(img1,'output/Part_2b/p2_board1.png');
imwrite(img2,'output/Part_2b/p2_board2.png');
imwrite(img3,'output/Part_2b/p2_board3.png');

figure;
imshow(img1);
figure;
imshow(img2);
figure;
imshow(img3);

function [img]=countPawns(img,black_on_white_pawn,black_on_black_pawn,white_on_black_pawn,white_on_white_pawn,count)

for i=421:-60:1;
    for j=1:60:421;
        if sum(abs(img(i:i+59,j:j+59)-black_on_white_pawn))<=100 | sum(abs(img(i:i+59,j:j+59)-black_on_black_pawn))<=100 | ...
                sum(abs(img(i:i+59,j:j+59)-white_on_black_pawn))<=100 | sum(abs(img(i:i+59,j:j+59)-white_on_white_pawn))<=100
            count=count+1
            text_str=string(count)
            position=[j i];
           img= insertText(img,position,text_str,'FontSize',10,'BoxColor',...
    'white','BoxOpacity',0.4,'TextColor','black');
            
         
        end
    end
end 

end

