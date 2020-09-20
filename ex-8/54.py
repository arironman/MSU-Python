num = int(input("Enter Number in Binary form: "))
x=1
temp=num
lst=[]
while x == 1:
    mod=temp%10
    temp=temp//10
    lst.append(mod)
    if temp == 0:
        break
lst.reverse()
for x in lst:
    if x == 0:
        print(1,end="")
    else:
        print(0,end="")
