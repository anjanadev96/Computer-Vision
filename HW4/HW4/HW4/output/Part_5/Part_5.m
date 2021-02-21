default_spectrogram('MC_water_mono.wav');

function [y]=default_spectrogram(input_audio_file)

y = audioread(input_audio_file);
disp(length(y))
y = y(:, 1);
figure;
spectrogram(y,256,100);

end