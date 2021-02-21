DFT([1,2-j,-j,-1+2j])

function [X]=DFT(x)
    N=length(x);
    for k=1:N
        X(k)=0;
        for n=1:N
            X(k)=X(k)+x(n).*exp(-1j.*2.*pi.*(n-1).*(k-1)./N);
        end
    end

end

