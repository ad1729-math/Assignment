import random


n=int(input("Enter the length of the array"))

def Random(n): 
    L=[]
    
    for i in range(0,n):
        v=random.randint(0,10**10)
        L.append(int(v/10**7)) 
    return L

M=Random(n)
print("An array of random numbers is",M)
