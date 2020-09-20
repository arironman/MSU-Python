from math import factorial
def strong(n):
    num=n
    sum=0
    while num != 0:
        temp=num%10
        num=num//10
        f=factorial(temp)
        sum+=f
    if sum == n:
        return True
    else:
        return False



n=int(input("Enter the Number: "))
if strong(n):
    print(f"{n} is a strong number ")
else:
    print(f"{n} is not a strong number")
