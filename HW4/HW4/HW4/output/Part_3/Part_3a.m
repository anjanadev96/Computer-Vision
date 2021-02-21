
%output=FastDFT([-0.0144+0.0709i, -0.1586-0.0502i, 0.5764, -0.1586-0.0502i, -0.4631-0.0709i, -0.1586-0.0502i, 0.5764, -0.1586-0.0502i])
%input=[-0.0144+0.0709i, -0.1586-0.0502i, 0.5764, -0.1586-0.0502i, -0.4631-0.0709i, -0.1586-0.0502i, 0.5764, -0.1586-0.0502i]
%output./input
FastIDFT([0, -4i, 0, 0, 0, 0, 0, 4i])
%FastIDFT([0.0409-0.2008i, 0.4487+0.1418i, -1.6303+0.0000i, 0.4487+0.1418i, 1.3097+0.2008i, 0.4487+0.1418i, -1.6303+0.0000i, 0.4487+0.1418i])
ifft([0, -4i, 0, 0, 0, 0, 0, 4i])
%ifft([0.0409-0.2008i, 0.4487+0.1418i, -1.6303+0.0000i, 0.4487+0.1418i, 1.3097+0.2008i, 0.4487+0.1418i, -1.6303+0.0000i, 0.4487+0.1418i])


function [X]=FastDFT(x)
    N=length(x);
    if N==1
        X=x;
        return 
    end
    omega_n=exp((-1j*2*pi)/N);
    omega=1;
    x_even=x(2:2:N);
    x_odd=x(1:2:N);
    X_even=FastDFT(x_even);
    X_odd=FastDFT(x_odd);
    for k=1:N/2
        X(k)=X_odd(k)+omega*X_even(k);
        X(k+ N/2)=X_odd(k)-omega*X_even(k);
        omega=omega*omega_n;
    end
    return 
end
      
function [x]=FastIDFT(X)
    N=length(X)
    X=conj(X)
    x=FastDFT(X)
    x=conj(x)
    x=x./N
    return 
end