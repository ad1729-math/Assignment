import numpy as np 
import matplotlib.pyplot as plt 
from fibo import Fibo 

N=[]
Fib=[]

 
for n in range(0,50):
    N.append(n)
    Fib.append(Fibo(n+1)[0]/Fibo(n)[0])

plt.plot(N,Fib,'r')
plt.show()


