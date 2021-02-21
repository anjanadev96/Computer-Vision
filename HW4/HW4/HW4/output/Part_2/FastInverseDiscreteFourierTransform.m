FastIDFT([2.0000 + 0.0000i,  -2.0000 - 2.0000i,  0.0000 - 2.0000i,  ...
          4.0000 + 4.0000i])
ifft([2.0000 + 0.0000i,  -2.0000 - 2.0000i,  0.0000 - 2.0000i,  ...
          4.0000 + 4.0000i])
      
      
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
      
      
function [x]=FastIDFT(X)
    N=length(X);
    X=conj(X)
    x=FastDFT(X)
    x=conj(x)
    x=x./N
    return 
end