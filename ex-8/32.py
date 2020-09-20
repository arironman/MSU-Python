#Frequency of digits in a number means how many times a digit comes in a given Number

num=int(input("Enter a Number: "))
lst=[]
temp=num
while temp != 0:
    mod=temp%10
    lst.append(mod)
    temp=temp//10
for x in range(0,10):
    print(f"Frequency of {x}: {lst.count(x)}")
