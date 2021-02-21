count_number_of_coins( 'NoMusic_1.mp4', 'NoMusic_1_output.avi', 'NoMusic_1_Audio.mp3')

function [out]= count_number_of_coins(input_video_file, output_video_file, input_audio_file)

[time_instances,no_of_samples]=get_time_instances(input_audio_file);
figure;
no_of_samples;
v= VideoReader(input_video_file);
out=VideoWriter(output_video_file);
out.FrameRate=v.FrameRate;
open(out)
currAxes = axes;
frame_no=0;
coins=0;
video_duration=v.Duration        
no_of_frames=v.NumFrames
x=no_of_samples/v.NumFrames;
frame_instances=int16(time_instances/x)
v.Duration/no_of_samples
   
while hasFrame(v)
    frame_no=frame_no+1
    vidFrame = readFrame(v);
    %image(vidFrame, 'Parent', currAxes);
    %currAxes.Visible = 'off';
    
    if ismember(frame_no,frame_instances)
        coins=coins+1
    end
text = append("Coins =",string(coins));
imFrame=insertText(vidFrame,[450 65],text,'FontSize',40,'TextColor','white', 'BoxOpacity', 0);
image(imFrame);
writeVideo(out,imFrame);

pause(1/v.FrameRate);
end
coins
close(out)

end


function [instances, no_of_samples]= get_time_instances(filename)
data= audioread(filename);
data=data(:,1);
[s,w,t]=spectrogram(data,256,100);
figure;
imagesc(flipud(log10(abs(s))));
s_real=log10(abs(s));
s_real=s_real>0;i
%[row,col]=find(s_real>0);
index=1;
instances=[];
no_of_samples=length(t');
%801-916 approx 8,9,10
%801-865- 23,24,25
%801-865- 39,40
%801-832- 54,55
%8,9,10,22,23,24
while index < no_of_samples
    time=50;

   if s_real(8,index) | ...
       s_real(9,index) | s_real(10,index) && s_real(23,index)| s_real(24,index) |s_real(25,index) &&...
       s_real(39,index)| s_real(40,index) && s_real(54,index) | s_real(55,index)


       instances= [instances, index];
       %To avoid risk of missing the coins because of very small distance
       %between consecutive coins on the spectrogram
       if index>9000 && index <9300
        time=30;
       else
        time=100;
       end
        
    end
    index=index+time;
end


end