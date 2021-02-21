img1=imread('input/Part_3/p3_board_1.jpg');
img2=imread('input/Part_3/p3_board_2.jpg');
img3=imread('input/Part_3/p3_board_3.jpg');

black_on_white_rook=imread('black_on_white_rook.png');
black_on_black_rook=imread('black_on_black_rook.png');
white_on_black_rook=imread('white_on_black_rook.png');
white_on_white_rook=imread('white_on_white_rook.png');
black_on_white_knight=imread('black_on_white_knight.png');
black_on_black_knight=imread('black_on_black_knight.png');
white_on_black_knight=imread('white_on_black_knight.png');
white_on_white_knight=imread('white_on_white_knight.png');
black_on_white_bishop=imread('black_on_white_bishop.png');
black_on_black_bishop=imread('black_on_black_bishop.png');
white_on_black_bishop=imread('white_on_black_bishop.png');
white_on_white_bishop=imread('white_on_white_bishop.png');
black_on_black_queen=imread('black_on_black_queen.png');
white_on_black_queen=imread('white_on_black_queen.png');
white_on_white_queen=imread('white_on_white_queen.png');

img1=IdentifyRooksBishopsQueens(img1,black_on_white_rook,black_on_black_rook,...
                                white_on_black_rook,white_on_white_rook,...
                                black_on_black_queen, white_on_black_queen,...
                                white_on_white_queen,black_on_white_bishop,...
                                black_on_black_bishop,white_on_black_bishop,...
                                white_on_white_bishop)
                            
img2=IdentifyRooksBishopsQueens(img2,black_on_white_rook,black_on_black_rook,...
                                white_on_black_rook,white_on_white_rook,...
                                black_on_black_queen, white_on_black_queen,...
                                white_on_white_queen,black_on_white_bishop,...
                                black_on_black_bishop,white_on_black_bishop,...
                                white_on_white_bishop)
img3=IdentifyRooksBishopsQueens(img3,black_on_white_rook,black_on_black_rook,...
                                white_on_black_rook,white_on_white_rook,...
                                black_on_black_queen, white_on_black_queen,...
                                white_on_white_queen,black_on_white_bishop,...
                                black_on_black_bishop,white_on_black_bishop,...
                                white_on_white_bishop)
                            
imwrite(img1,'output/Part_3b/p3_board1.png');
imwrite(img2,'output/Part_3b/p3_board2.png');
imwrite(img3,'output/Part_3b/p3_board3.png');

figure();
imshow(img1);
figure();
imshow(img2);
figure();
imshow(img3);


function [img]=IdentifyRooksBishopsQueens(img,black_on_white_rook,black_on_black_rook,...
                                           white_on_black_rook,white_on_white_rook,...
                                          black_on_black_queen, white_on_black_queen,...
                                          white_on_white_queen,black_on_white_bishop,...
                                          black_on_black_bishop,white_on_black_bishop,...
                                          white_on_white_bishop)

for i=1:60:421;
    for j=1:60:421;
        if sum(abs(img(i:i+59,j:j+59)-black_on_white_rook))<=100 | sum(abs(img(i:i+59,j:j+59)-black_on_black_rook))<=100 | ...
            sum(abs(img(i:i+59,j:j+59)-white_on_black_rook))<=100 | sum(abs(img(i:i+59,j:j+59)-white_on_white_rook))<=100 
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
        
        if sum(abs(img(i:i+59,j:j+59)-black_on_black_queen))<=100 | ...
            sum(abs(img(i:i+59,j:j+59)-white_on_black_queen))<=100 | sum(abs(img(i:i+59,j:j+59)-white_on_white_queen))<=100 
            img=insertShape(img, 'Rectangle',[j, i, 58, 58],'Color','red', 'LineWidth',2);
        end
        
        if sum(abs(img(i:i+59,j:j+59)-black_on_white_bishop))<=100 | sum(abs(img(i:i+59,j:j+59)-black_on_black_bishop))<=100 | ...
            sum(abs(img(i:i+59,j:j+59)-white_on_black_bishop))<=100 | sum(abs(img(i:i+59,j:j+59)-white_on_white_bishop))<=100 
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'Color','blue', 'LineWidth',2);
        end
    end
end
end





