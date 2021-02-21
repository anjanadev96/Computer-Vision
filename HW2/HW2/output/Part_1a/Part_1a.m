img=imread('input/Part_1/p1_board.jpg');
figure;
imshow(img);

img1=insertlabels(img);
imwrite(img1,'output/Part_1a/Part_1a.png');
figure;
imshow(img1);


function [img1]= insertlabels(img)
str= [];
position=[];
for i=8:-1:1
    for j='a':1:'h'
        str=[ str, string(j)+string(i)];
    end
end
str=reshape(str,64,1);

for i=1:60:480
    for j=1:60:480
        position=[position; [j  i]];
    end
end
position=reshape(position,64,2);
disp(position)    
img1= insertText(img,position,str,'BoxColor', 'white','FontSize', 12, 'TextColor', 'black'); 
figure;

end
