def count(n):
    c=0
    while n != 0:
        n=n//10
        c+=1
    return c

def reverse(n):
    dig=count(n)
    dig-=1
    sum=0
    for i in range(0,dig+1):
        temp=n%10
        n=n//10
        sum+=(temp*(10**dig))
        dig-=1
    return sum
print(reverse(int(input("Enter  a Number: "))))
