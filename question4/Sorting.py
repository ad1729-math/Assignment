import random 

def Sort(M):
   j=0
   n=len(M)
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
   return M 

R=[]
for i in range(0,20):
    R.append(int(random.randint(0,10**10)/10**7))

print("An unsorted array of 20 random numbers is=",R)
print("The sorted array of these random numbers is=",Sort(R))