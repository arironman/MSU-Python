#Arthimatic operators
num1=int(input("\t \tEnter Number 1: "))
num2=int(input("\t\t Enter Number 2:"))

print("\t Addition Operator:")
add=num1+num2   #we do not preffer to use sum as a variable or function name
                #because sum is a function name
print(f"Addition of Number 1 and Number 2 is: {add}")


print("\t Subtraction Operator: ")
sub=num1-num2
print(f"Subtraction of Number 1 and Number 2 is: {sub}")


print("\t Multiplication Operator: ")
multi=num1*num2
print(f"Multiplication of Number 1 and Number 2 is: {multi}")


print("\t Division Operator: ")
div=num1/num2
print(f"Division of Number 1 and Number 2 is: {div}")


print("\t Modulus Operator: ")
mod=num1%num2
print(f"Modulus of Number 1 and Number 2 is: {mod}")


print("\t Floor Division Operator: ")
fdiv=num1//num2
print(f"Floor Division of Number 1 and Number 2 is: {fdiv}")


print("\t Power/Exponent Operator: ")
exp=num1**num2
print(f"Exponent of Number 1 and Number 2 is: {exp}")

