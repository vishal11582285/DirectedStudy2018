import numpy as np
# from numpy import random
import random
import itertools
# Number of possible states : (k+2) where K: number of days
K = 4
k_val = range(-1, K + 1)
k_val = np.array(k_val)
print(k_val)

# N rows of M beds eacs
N,M = 10,10

# Threshhold of susceptibility
T = 0.8

neighbors = lambda x, y: [(x2, y2) for x2 in range(x - 1, x + 2)
                              for y2 in range(y - 1, y + 2)
                              if (-1 < x < M and
                                  -1 < y < N and
                                  (x != x2 or y != y2) and
                                  (0 <= x2 < M) and
                                  (0 <= y2 < N))]

def calc_proportions(MatPat):
    # global It
    It = (MatPat >= 1).sum() / (MatPat.shape[0] * MatPat.shape[1])
    # global St
    St = (MatPat == 0).sum() / (MatPat.shape[0] * MatPat.shape[1])
    # global Rt
    Rt = (1 - It - St)

    return [It,St,Rt]


def simulate(A,kval):
    # print(A)
    # print(list(range(M)),list(range(N)))
    for i in range(M):
        for j in range(N):
            # print(i,j,end='\n')
            neigh=neighbors(i,j)
            # print(neigh,end='\n')
            for t in neigh:
                if(A[i,j]>=1):
                    # print(t[0],t[1],end='\n')
                    if(A[t[0],t[1]] != -1 and A[t[0],t[1]]==0):
                        if(np.random.random() < T):
                            A[t[0],t[1]]=-2

    for i in range(M):
        for j in range(N):
            if(A[i,j]>=1):
                A[i,j]=kval[(int(A[i,j])+2)%(K+2)]
    A[A==-2]=1
    x, y, z= calc_proportions(A)
    global It
    It=x
    global St
    St = y
    global Rt
    Rt = z

    print(A)
    # print(It,St,Rt)
    return A

# print(neighbors(5,5))

#It defines Infected population, St defines population never infected, and the remaining population is:
#Rt = (1 - It - St)
#Mod function can help traverse the list recursively
MatPat=np.matrix(np.array([np.random.randint(low=0,high=1,size=M*N)])).reshape((M,N))

MatPat[int(M/2),int(N/2)]=1
# MatPat[8,5]=1
# MatPat[5,8]=1
print(MatPat)
print(MatPat.shape)

It=(MatPat == 1).sum()/ (MatPat.shape[0]*MatPat.shape[1])
St=(MatPat == 0).sum()/ (MatPat.shape[0]*MatPat.shape[1])
Rt=(1 - It - St)
print(It,St,Rt)

A=np.asmatrix(MatPat)
# print(A)

#Finding neighbors of subject in matrix
storeRt,storeIt,storeSt=[],[],[]
lim=0
while(It>0.0):
    A=simulate(A,k_val)
    lim+=1
    # print(A)
    storeRt = storeRt + [Rt]
    storeIt = storeIt + [It]
    storeSt = storeSt + [St]



# print(A)
# print(k_val[2])

import matplotlib.pyplot as plt;
plt.rcdefaults()
import matplotlib.pyplot as plt

objects = ('Recovered', 'Infected', 'Susceptible')
y_pos = np.arange(len(objects))
performance = [Rt,It,St]

# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
plt.ylabel('Proportion')
plt.title('SIR Simulation')

# print(storeSt)
plt.plot(np.array(range(lim)),storeRt,label='Recovered')
plt.plot(np.array(range(lim)),storeIt,label='Infected')
plt.plot(np.array(range(lim)),storeSt,label='Susceptible')
plt.legend(['Recovered','Infected','Susceptible'], loc=3, borderaxespad=2)
plt.show()

print([Rt,It,St])