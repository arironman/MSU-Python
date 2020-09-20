num=int(input("Enter the Number: "))
multi=1
while num != 0:
    multi=multi*(num%10)
    num=num//10
print(f"Multiplication of all the Digits of a Number are: {multi}")
