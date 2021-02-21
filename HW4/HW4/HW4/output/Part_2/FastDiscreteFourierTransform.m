%FastDFT([1,2-1j,-1j,-1+2j])
%fft([1,2-1j,-1j,-1+2j])


function [X]=FastDFT(x)
    N=length(x);
    if N==1
        X=x;
        return 
    end
    omega_n=exp(-1j*2*pi/N)
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
