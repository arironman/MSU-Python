num=int(input("Enter a Number: "))
temp=num
lst=[]
for x in range(1,num+1):
    if temp%x == 0:
        lst.append(x)

print(f"The factors of {num} are: ",end="")
for x in lst:
    print(x,end=", ")
