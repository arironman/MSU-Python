mantisa=int(input("Enter the Base/Mantisa of a Number: "))
power=int(input("Enter the power of a number: "))
result=1
for x in range(0,power):
    result*=mantisa
print(f"{mantisa} power of {power} is: {result}")
