num=int(input("Enter a Number: "))
count=0
n=num
while n != 0:
    n=n//10
    count=count+1

n=num
rev=0
var=count
count=count-1
for x in range(var,0,-1):
    mod=n%10
    n=n//10
    rev=rev+(mod*(10**count))
    count-=1
print(f"Reverse of a number is: {rev}")
