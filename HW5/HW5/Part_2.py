import numpy as np

def forward( M,N,Obs,A,B,pi):
    states=[]
    for i in range(M):
        states.append(i)

    alpha = [{}]
    for state in states:
        alpha[0][state] = pi[state] * B[state][Obs[0]]
    for t in range(1, N):
        alpha.append({})
        for state in states:
            alpha[t][state] = sum((alpha[t -1][state0] * A[state0][state] * B[state][Obs[t]]) for state0 in states)
    prob = sum((alpha[N-1][s]) for s in states)
    return alpha,prob

M=2
N=7

Obss=[[1,0,0,0,1,0,1],[0,0,0,1,1,2,0],[1,1,0,1,0,1,2],[0,1,0,2,0,1,0],[2,2,0,1,1,0,1]]
#
Hmms=[
    [
        [[1.0, 0.0], [0.5, 0.5]],
        [[0.4, 0.6, 0.0], [0.0, 0.0, 1.0]],
        [0.0, 1.0]
    ],
    [
        [[0.25, 0.75], [1.0, 0.0]],
        [[0, 1.0, 0], [0.66, 0.0, 0.34]],
        [1.0, 0.0]
     ],
[
    [[0.0, 1.0], [1.0, 0.0]],
    [[1.0, 0.0, 0.0],[0.0, 0.66, 0.34]],
    [1.0, 0.0]
],
[
    [[1, 0], [0.44, 0.56]],
    [[0.36, 0.42, 0.22], [1.0, 0, 0]],
    [0, 1.0]
],
[
    [[0.0, 1.0], [1.0, 0.0]],
    [[0.25, 0.75, 0.0], [1.0, 0.0, 0.0]],
    [1.0, 0.0]
]
]

# Obs=(1,0,0,0,1,0,1)
# A = [[0.6, 0.4],
#      [1, 0]]
# B = [[0.7, 0.3, 0],
#      [0.1, 0.1, 0.8]]
# pi = [0.7, 0.3]


#
# alpha,answer=forward(M,N,Obs,A,B,pi)
# print("Alpha")
# for i in range(len(alpha)):
#     print(alpha[i])
#
# print(answer)

ans=[[0]*len(Obss) for i in range(len(Hmms))]
answer=0

# for j in range(len(Obss)):
#     Obs=Obss[j]
#     alpha,ans=forward(M,N,Obs,A,B,pi)
#     print("Likelihood for 0"+str(j),"is:", ans)



for j in range(len(Obss)):
    for i in range(len(Hmms)):
        Obs = Obss[j]
        Hmm=Hmms[i]
        alpha,ans[j][i]=forward(M,N,Obs,Hmm[0],Hmm[1],Hmm[2])

        # ans[j][i]=answer

#
for i in range(len(ans)):
    print(ans[i])











