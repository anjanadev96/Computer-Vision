img2=imread('p3_board_1.jpg');
img1=imread('p3_board_3.jpg');
img=im2bw(img2);
rook1=img(1:60,1:60);
rook2=img(1:60,301:360);
rook3=img(421:480,1:60);
rook4=img(421:480,301:360);
pawn1= img(121:180,1:60);




bishop1=img(61:120,181:240);
bishop2=img(1:60,301:360);
bishop3=img(421:480,1:60);
bishop4=img(421:480,301:360);


queen1=img(61:120,241:300);
queen2=img(1:60,301:360);


%for i=1:60:421;
    %for j=1:60:421;
        %if sum(abs(img1(i:i+59,j:j+59)-rook1))<=100 | sum(abs(img1(i:i+59,j:j+59)-rook2))<=100 | ...
            %sum(abs(img1(i:i+59,j:j+59)-rook3))<=100 | sum(abs(img1(i:i+59,j:j+59)-rook4))<=100 
            %img1=insertShape(img1, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        %end
    %end
%end
%figure;
%imshow(img1)%



