img1=imread('p2_board_1.jpg');
img2=imread('p2_board_2.jpg');
img3=imread('p2_board_3.jpg');

black_on_white_pawn=imread('black_on_white_pawn.png');
black_on_black_pawn=imread('black_on_black_pawn.png');
white_on_black_pawn=imread('white_on_black_pawn.png');
white_on_white_pawn=imread('white_on_white_pawn.png');

img1=InsertBoxes(img1,black_on_white_pawn,black_on_black_pawn,white_on_black_pawn,white_on_white_pawn);
img2=InsertBoxes(img2,black_on_white_pawn,black_on_black_pawn,white_on_black_pawn,white_on_white_pawn);
img3=InsertBoxes(img3,black_on_white_pawn,black_on_black_pawn,white_on_black_pawn,white_on_white_pawn);

imwrite(img1,'output/Part_2a/p2_board1.png');
imwrite(img2,'output/Part_2a/p2_board2.png');
imwrite(img3,'output/Part_2a/p2_board3.png');



figure;
imshow(img1);
figure;
imshow(img2);
figure;
imshow(img3);


function [img]=InsertBoxes(img,black_on_white_pawn,black_on_black_pawn,white_on_black_pawn,white_on_white_pawn)
for i=1:60:421;
    for j=1:60:421;
        if sum(abs(img(i:i+59,j:j+59)-black_on_white_pawn))<=100
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
        if  sum(abs(img(i:i+59,j:j+59)-black_on_black_pawn))<=100
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
        if  sum(abs(img(i:i+59,j:j+59)-white_on_black_pawn))<=100
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
        if  sum(abs(img(i:i+59,j:j+59)-white_on_white_pawn))<=100
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);   
        end
    end
end 

end


            