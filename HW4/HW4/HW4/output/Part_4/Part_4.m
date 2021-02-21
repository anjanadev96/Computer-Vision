get_spectrogram('/HW4/input/Part_4/MC_water_mono.wav')

function [sgram]=get_spectrogram(input_audio_file)

y = audioread(input_audio_file);
y = y(:, 1);


wstep = 100;
wsize = 256;
nsamp = length(y);
nwin = floor(nsamp/wstep);
nbins = wsize/2 + 1;

sgram = zeros(nwin, nbins);
win = hamming(wsize);

for k=0:(nwin-1)
    wstart = k*wstep+1;
    wstop = wstart + wsize - 1;
    x = y(wstart:min(nsamp,wstop));
    
    if length(x) < wsize
        x = [x; zeros(wsize - length(x), 1)];
    end

    x = x .* win;
    
    xhat = FastDFT(x);
    sgram(k+1, :) = log10(abs(xhat(1:nbins)));
end


figure;
imagesc(sgram);
set(gca,'YDir','normal');
end


function [X]=FastDFT(x)
    N=length(x);
    if N==1
        X=x;
        return 
    end
    omega_n=exp(-1j*2*pi/N);
    omega=1;
    x_even=x(2:2:N);
    x_odd=x(1:2:N);
    X_odd=FastDFT(x_odd);
    X_even=FastDFT(x_even);
    for k=1:N/2
        X(k)=X_odd(k)+omega.*X_even(k);
        X(k+ N/2)=X_odd(k)-omega.*X_even(k);
        omega=omega.*omega_n;
    end
    return 
end
