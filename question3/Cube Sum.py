def f(n):
    sum=0 
    for i in range(1,n):
        sum=sum+i**3
    return sum
n=int(input("Enter the number"))
print(f(n))

#Now the sum of cubes of numbers from 11 to 40 is 
A=f(40)-f(11)

print("Sum of cubes of numbers from 11 to 40 is=",A)