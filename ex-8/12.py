num=int(input("Enter a Number: "))
fact=1
for x in range(1,num+1):
    fact*=x    #fact=fact*x

print(f"Factorial of {num} is {fact}")
