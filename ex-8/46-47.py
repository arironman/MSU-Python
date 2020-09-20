start = int(input("From where u wanna to check the Number: "))
end = int(input("Till where u wanna to check: "))

lst=[]
for i in range(start,end+1):
    add=0
    n=i
    for x in range(0,3): 
        temp=n%10
        n=n//10
        add=add+(temp**3)
    if add == i:
        lst.append(i)
for x in lst:
    print(x,end=",")
