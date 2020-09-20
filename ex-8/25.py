n=int(input("Enter a Number: "))
#For First digit
num=n    #here i store origina;l value into an variable
        #because we need it again
while num>10:
    num=num//10
print(f"First Digit is {num}")




#For Second Digit
num=n
print(f"Last Digit is {num%10}")
