#using while loop
num=int(input("Enter the Number: "))
temp=num
fact=1
while temp != 1:
    fact=fact*temp
    temp-=1
print(f"Factorial of a Number is {fact}")






#using Math Module
print("Factorial Using Math Module")
from math import factorial
n=int(input("Enter the Number: "))
print(f"Factorial of a Number is {factorial(n)}")
