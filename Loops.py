def f(n):
    sum=0 
    for i in range(1,n):
        sum=sum+i**3
    return sum
n=int(input("Enter the numbe"))
print(f(n))
