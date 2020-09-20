#strong number condition and eg 145=1!+4!+5!
num = int(input("Enter the Number: "))
x=1
n=num
sum=0
lst=[]
while x == 1:
    mod=n%10
    lst.append(mod)
    n=n//10
    if n == 0:
        break
for x in lst:
    multi=1
    for i in range(1,x+1):
        multi= multi*i
    sum+=multi

if sum == num:
    print(f"{num} is a Strong Number: ")
else:
    print(f"{num} is not a strong Number: ")
    
