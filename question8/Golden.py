import math as m
import numpy as np
import matplotlib.pyplot as plt 

from Fibonacci import Fibo 


def Ratio(N):
    R=[]
    for i in range(0,len(N)):
        n=N[i]
        v=Fibo(n+1)/Fibo(n)
        R.append(v)
    return R


phi=(1+m.sqrt(5))/2

N=np.arange(0,50,1)
R=Ratio(N)

plt.plot(N,R,'ro-',label="Ratio of consecutive numbers of the sequence")
plt.plot(N,N/N*phi,'b',label="The value to which it converges, Golden ratio")
plt.xlabel("n --->")
plt.ylabel("Ration of consecutive Fibonacci numbers")
plt.legend()
plt.show()




