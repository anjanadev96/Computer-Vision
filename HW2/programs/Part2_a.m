img=imread('p2_board_3.jpg');
img1=imread('p2_board_1.jpg');
img1=im2bw(img1,0.55);
img2= im2bw(img,0.55);


p1=img1(61:120,421:480);
p2=img1(61:120,1:60);
p3=img1(361:420,61:120);
p4=img1(361:420,121:180);

for i=1:60:421;
    for j=1:60:421;
        if sum(abs(img2(i:i+59,j:j+59)-p1))<=10
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
        if  sum(abs(img2(i:i+59,j:j+59)-p2))<=10
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
        if  sum(abs(img2(i:i+59,j:j+59)-p3))<=10
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);
        end
        if  sum(abs(img2(i:i+59,j:j+59)-p4))<=10
            img=insertShape(img, 'Rectangle',[j, i, 58, 58], 'LineWidth',2);   
        end
    end
end 

figure;
imshow(img);

            