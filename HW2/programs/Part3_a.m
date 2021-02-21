img=imread('p3_board_1.jpg');
img1=imread('p3_board_3.jpg');
rook1=img(1:60,1:60);
rook2=img(1:60,301:360);
rook3=img(421:480,1:60);
rook4=img(421:480,301:360);

for i=1:60:421;
    for j=1:60:421;
        if sum(abs(img1(i:i+59,j:j+59)-rook1))<=100 | sum(abs(img1(i:i+59,j:j+59)-rook2))<=100 | ...
            sum(abs(img1(i:i+59,j:j+59)-rook3))<=100 | sum(abs(img1(i:i+59,j:j+59)-rook4))<=100 
            img1=insertShape(img1, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
    end
end
figure;
imshow(img1)



