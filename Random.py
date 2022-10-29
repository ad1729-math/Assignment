import random
from re import L

n=int(input("Enter the length of the array"))

def Random(n): 
    L=[]
    
    for i in range(0,n):
        v=random.randint(0,10**10)
        L.append(int(v/10**7)) 
    return L

M=Random(n)
print("The unsorted array of random numbers is",M)
j=0
while j<n:
   i=0
   for i in range(0,n-1):
        if M[i]>M[i+1]:
           a=M[i+1]
           M[i+1]=M[i]
           M[i]=a 
        else:
             continue 
   j+=1

print("The array of random number after sorting is",M)