import numpy as np 
import math as m

n=int(input("Enter the number"))

def Sieve(n):

   L=[]
   for i in range(2,n+1):
       L.append(i)

   i=0
   while i<len(L):
      p=L[i]
      j=p
      for j in range(p,int(n/p)+1):
         if j*p in L:
            L.remove(j*p)
         else:
           continue
      i=i+1

   return L


print("Primes upto "+str(n),"are",Sieve(n))
M=Sieve(200)
print("Primes upto 200 are",M)
