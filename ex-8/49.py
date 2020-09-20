start = int(input("From where u wanna to check the Perfect Number: "))
end = int(input("Till where u wanna to check: "))
perfect=[]
for num in range(start,end+1):
    lst=[]
    for x in range(1,num):
        if num%x == 0:
            lst.append(x)
    sum=0
    for x in lst:
        sum+=x
    if sum == num:
        perfect.append(num)
print(f"Perfect Number b/w {start} and {end} are: ",end="")
for x in perfect:
    print(x,end=" ")

