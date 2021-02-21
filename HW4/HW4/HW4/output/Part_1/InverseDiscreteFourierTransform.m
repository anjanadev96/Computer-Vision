IDFT([2.0000 + 0.0000i,  -2.0000 - 2.0000i,  0.0000 - 2.0000i,  4.0000 + 4.0000i
])

function [x]=IDFT(X)
    N=length(X);
    for n=1:N
        x(n)=0;
        for k=1:N
            x(n)=x(n)+X(k).*exp(1j.*2.*pi.*(n-1).*(k-1)./N);
        end
        x(n)=x(n)./N
    end
    
end