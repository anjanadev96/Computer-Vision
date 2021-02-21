import Part_EC1 as f

def forward_backward_normalization(A,B,pi,M,N,Obs):
    T = len(Obs)
    beta = [[None ] *T for _ in range(N)]

    logL, sum = f.forward_normalization(A, B, pi, M, N, Obs)

    for i in range(N):
        beta[i][T-1] = sum[T-1]
    for t in range(T-1, 0, -1):
        for i in range(N):
            beta[i][t -1] = 0
            for j in range(N):
                beta[i][ t -1] += A[i][j] * B[j][Obs[t]] * beta[j][t]

            beta[i][ t -1] *= sum[t -1]

    return logL,beta

M = 3
N = 2
Obs = [0, 1, 0, 2, 0, 1, 0]

A = [[0.66, 0.34],
     [1, 0]]
B = [[0.5, 0.25, 0.25],
     [0.1, 0.1, 0.8]]
pi = [0.8, 0.2]

logL,beta=forward_backward_normalization(A,B,pi,M,N,Obs)
print("Beta values for the observation sequence are:")
for i in range(len(beta)):
    print(beta[i])

