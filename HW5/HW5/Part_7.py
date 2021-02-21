import numpy as np
import random
import nanohmm

#Enter the size of the A,B, pi matrices as input parameters
def randomize(m,n):
      A=[]
      for i in range(m):
          a= [ random.random() for i in range(n)]
          s=sum(a)
          a= [ i/s for i in a]
          A.append(a)
      return A

A=randomize(4,4)
B=randomize(4,6)
pi=randomize(1,4)[0]


Observation_sequences=[
(4,2,5,1,5,1,5,3,2,3,2,0,1,0,0,4,4,3,0,1),
(3,2,3,3,5,5,5,5,1,0,1,4,2,4,3,0,5,3,1,0),
(4,3,0,3,4,0,1,0,2,0,5,3,2,0,0,5,5,3,5,4),
(3,4,2,0,5,4,4,3,1,5,3,3,2,3,0,4,2,5,2,4),
(2,0,5,4,4,2,0,5,5,4,4,2,0,5,4,4,5,5,5,5)]

def Baum_Welch(A,B,pi,Observation_sequences):
      for j in range(len(Observation_sequences)):
            O=Observation_sequences[j]
            lambda_ = nanohmm.hmm_t(A, B, pi)
            bw = nanohmm.baumwelch_t(lambda_)
            LL, lambda_ = nanohmm.baumwelch(bw, O, 100)
            print("LL =", LL)
            print("Trained HMM for O"+str(j+1))
            print("A = ", lambda_.A)
            print("B = ", lambda_.B)
            print("pi = ", lambda_.pi)

Baum_Welch(A,B,pi,Observation_sequences)

