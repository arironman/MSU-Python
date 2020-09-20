num=int(input("Enter the Number: "))
add=0
while num != 0:
    add=add+(num%10)
    num=num//10
print(f"Sum of all the Digits of a Number are: {add}")
