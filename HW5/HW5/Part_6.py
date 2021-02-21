import nanohmm

Obss= [[4,2,5,1,5,1,5,3,2,3,2,0,1,0,0,4,4,3,0,1],
       [3,2,3,3,5,5,5,5,1,0,1,4,2,4,3,0,5,3,1,0],
       [4,3,0,3,4,0,1,0,2,0,5,3,2,0,0,5,5,3,5,4],
       [3,4,2,0,5,4,4,3,1,5,3,3,2,3,0,4,2,5,2,4],
       [2,0,5,4,4,2,0,5,5,4,4,2,0,5,4,4,5,5,5,5]]

Hmms=[
[
[[0.33, 0, 0, 0.67, 0],
      [0.67, 0, 0.33, 0, 0],
      [0, 1.0, 0.0, 0, 0],
      [0, 0, 0, 0.25, 0.75],
      [0.0, 0.0, 0.6, 0, 0.4]],
[[0.67, 0, 0, 0, 0, 0.33],
      [0.0, 1.0, 0, 0, 0, 0],
      [0.5, 0, 0, 0, 0, 0.5],
      [0, 0, 0, 0.25, 0.75, 0],
      [0, 0.0, 0.6, 0.4, 0, 0.0]],
[0.0, 0.0, 0.0, 1.0, 0.0]
],

[
[[0.0, 0.0, 1.0, 0, 0.0],
      [0.0, 0, 0.0, 0.0, 1.0],
      [0.38, 0.0, 0.23, 0.38, 0.0],
      [0.0, 0.31, 0.0, 0.69, 0],
      [0.0, 0.75, 0.0, 0.25, 0.0]],
[[0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
      [0.0, 0.6, 0.2, 0.2, 0.0, 0.0],
      [0.0, 0.0, 0, 1.0, 0.0, 0],
      [0, 0.0, 0, 0.22, 0.0, 0.78],
      [0.6, 0.0, 0.0, 0.0, 0.4, 0.0]],
[0.0, 0.0, 1.0, 0.0, 0.0]
],

[
[[0, 0.0, 0.32, 0.18, 0.5],
      [0.0, 0.0, 0.0, 1.0, 0.0],
      [0, 0.0, 0, 0.0, 1.0],
      [0, 0.64, 0, 0.0, 0.36],
      [1.0, 0.0, 0, 0, 0]],
[[0.0, 0.17, 0.33, 0.0, 0.0, 0.5],
      [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
      [0.47, 0.0, 0.0, 0.0, 0.0, 0.53],
      [0.27, 0.0, 0.0, 0.0, 0.73, 0.0],
      [0.66, 0.0, 0.0, 0.33, 0.0, 0.0]],
[0.0, 0.0, 0.0, 1.0, 0.0]
],

[
[[0.0, 0.0, 1.0, 0, 0.0],
      [0.0, 0, 0.62, 0, 0.38],
      [0.0, 0.5, 0.0, 0.5, 0.0],
      [0.0, 0.23, 0.0, 0.0, 0.77],
      [0.0, 0, 0, 1.0, 0]],
[[0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
      [0.0, 0.0, 0.62, 0, 0.38, 0.0],
      [0, 0.0, 0.0, 0.0, 1, 0],
      [0, 0.0, 0, 0.41, 0.18, 0.41],
      [0.31, 0.16, 0.37, 0.16, 0, 0.0]],
[1.0, 0.0, 0.0, 0.0, 0]
],

[
[[0.5, 0.33, 0, 0.17, 0.0],
      [0.0, 0.0, 0.0, 0.0, 1.0],
      [0.75, 0.0, 0.25, 0.0, 0.0],
      [0.0, 0.0, 0, 1.0, 0.0],
      [0.0, 0.0, 1.0, 0.0, 0.0]],
[[0.0, 0.0, 0.0, 0.0, 1.0, 0],
      [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0, 1.0],
      [0.0, 0.0, 0.0, 0.0, 0, 1.0],
      [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
[0.0, 1.0, 0.0, 0.0, 0.0]
]

]

ans=[[0]*len(Obss) for i in range(len(Hmms))]
answer=0

for j in range(len(Obss)):
    for i in range(len(Hmms)):
        Obs = Obss[j]
        Hmm=Hmms[i]
        lambda_ = nanohmm.hmm_t(Hmm[0], Hmm[1], Hmm[2])
        f = nanohmm.forward_t(lambda_)
        LL = nanohmm.forward(f, Obs)
        ans[j][i]=LL

for i in range(len(ans)):
    print(ans[i])