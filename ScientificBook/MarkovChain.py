import numpy as np

p=0.004
R=3
S0=99
I0=1
j=1
N=(S0+I0)
size=R+2
MIXES_WITH=(0.1*N)

def markov_matrix():
    mat = np.matrix(np.zeros(shape=(size,size)))
    population = np.matrix(np.zeros(shape=(1, size)))
    population[0,0]=S0
    population[0,1]=I0
    # j=3

    for i in range(1,R+1):
        mat[i,i+1]=1
    mat[size-1]=mat[size-2]
    # print(mat)
    # print(population)
    return mat,population

def transition(j,mat,population):
    mat[0, 1] = 1 - (np.power((1 - p), j))
    mat[0, 0] = (1 - mat[0, 1])
    # for i in range(j):
    population=np.dot(population,mat)
    # print(population)
    return population

mat,population=markov_matrix()

# random_list=np.array(range(20))

I=I0
day=0
modelSIR=list()
modelSIR.append([S0,I0,0])
while(I>=1):
    a=np.random.randint(low=0,high=MIXES_WITH)
    # print(a)
    population=transition(a,mat,population)
    S=population[0,0]
    R=population[0,size-1]
    I= (N - S - R)
    # print(population)
    # print(S,I,R)
    day+=1
    modelSIR.append([S,I,R])

print(modelSIR)
S_list=[x[0] for x in modelSIR]
I_list=[x[1] for x in modelSIR]
R_list=[x[2] for x in modelSIR]
print('Epidemic lasted for {} days'.format(day))

import matplotlib.pyplot as p
# p.style.use('ggplot')
p.rcParams["figure.figsize"] = (12,10)
p.plot(S_list,label='Susceptible')
p.plot(I_list,label='Infected')
p.plot(R_list,label='Recovered')
p.xlabel('Days')
p.ylabel('Population Size')
p.xticks(np.arange(day),range(0,day))
p.legend()
p.show()
p.close()