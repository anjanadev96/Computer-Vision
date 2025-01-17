img1=imread('input/Part_3/p3_board_1.jpg');
img2=imread('input/Part_3/p3_board_2.jpg');
img3=imread('input/Part_3/p3_board_3.jpg');

black_on_white_rook=imread('black_on_white_rook.png');
black_on_black_rook=imread('black_on_black_rook.png');
white_on_black_rook=imread('white_on_black_rook.png');
white_on_white_rook=imread('white_on_white_rook.png');

img1=HighlightRooks(img1,black_on_white_rook,black_on_black_rook,white_on_black_rook,white_on_white_rook)
img2=HighlightRooks(img2,black_on_white_rook,black_on_black_rook,white_on_black_rook,white_on_white_rook)
img3=HighlightRooks(img3,black_on_white_rook,black_on_black_rook,white_on_black_rook,white_on_white_rook)

imwrite(img1,'output/Part_3a/p3_board1.png');
imwrite(img2,'output/Part_3a/p3_board2.png');
imwrite(img3,'output/Part_3a/p3_board3.png');

figure();
imshow(img1);
figure();
imshow(img2);
figure();
imshow(img3);



function [img]=HighlightRooks(img,black_on_white_rook,black_on_black_rook,white_on_black_rook,white_on_white_rook)
for i=1:60:421;
    for j=1:60:421;
        if sum(abs(img(i:i+59,j:j+59)-black_on_white_rook))<=100 | sum(abs(img(i:i+59,j:j+59)-black_on_black_rook))<=100 | ...
            sum(abs(img(i:i+59,j:j+59)-white_on_black_rook))<=100 | sum(abs(img(i:i+59,j:j+59)-white_on_white_rook))<=100 
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
    end
end
end




