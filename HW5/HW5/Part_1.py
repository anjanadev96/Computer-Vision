import itertools
import numpy as np


def forward(M,N,O,A,B,pi):
    states=[]

    for i in range(M):
        states.append(i)

    state_permutations=[]


    for r in itertools.product(states, repeat=N):
        state_permutations.append(r)
    state_sequence_prob=[0]*len(state_permutations)


    for i in range(len(state_permutations)):
        state_sequence_prob[i]=pi[state_permutations[i][0]]*B[state_permutations[i][0]][O[0]]

    for i in range(len(state_permutations)):
        for j in range(1,len(state_permutations[0])):
            state_sequence_prob[i]*=A[state_permutations[i][j-1]][state_permutations[i][j]]*B[state_permutations[i][j]][O[j]]

    return sum(state_sequence_prob)
    #return np.log2(sum(state_sequence_prob))

M=2
N=7
O=[0,1,0,2,0,1,0]

A = [[0.66, 0.34],
     [1, 0]]
B = [[0.5, 0.25, 0.25],
     [0.1, 0.1, 0.8]]
pi = [0.8, 0.2]
answer=forward(M,N,O,A,B,pi)
print(answer)