f0=1
f1=1

def F(n):
    A=f0
    B=f1
    for i in range(1,n):
       C=B
       B=B+A
       A=C
       
    return B
    
print("The 10th, 20th and 30th Fibonacci numbers are respectively", F(10), F(20), F(30))


