import numpy as np

def forward_normalization(A, B, pi, M, N, Obs):
    T = len(Obs)  #Length of Observation Sequence
    alpha = [[0] * T for _ in range(N)]
    sum = [0] * T
    logL = 0
    for t in range(T):
        sum[t] = 0
        for i in range(N):
            if t == 0:
                alpha[i][0] = pi[i] * B[i][Obs[0]]
            else:
                alpha[i][t] = 0
                for j in range(N):
                    alpha[i][t] += alpha[j][t - 1] * A[j][i] * B[i][Obs[t]]
            sum[t] += alpha[i][t]
        if sum[t] == 0 or float('inf') == 1.0 / sum[t]:
            sum[t] = 1.0
            logL = -float('inf')
        else:
            sum[t] = 1.0 / sum[t]
            for i in range(N):
                alpha[i][t] *= sum[t]
        logL -= np.log2(sum[t])

    return logL,sum


M = 3 #Range of values in the Observation Sequence
N = 2 #Number of States
Obs = [0, 1, 0, 2, 0, 1, 0]

A = [[0.66, 0.34],
     [1, 0]]
B = [[0.5, 0.25, 0.25],
     [0.1, 0.1, 0.8]]
pi = [0.8, 0.2]
x,_ = forward_normalization(A, B, pi, M, N, Obs)
print("Log Likelihood of Observation Sequence is:",x)
