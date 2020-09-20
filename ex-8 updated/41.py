n=int(input("Enter a number: "))
x=0
fact=1
while x == 0:
    fact*=n
    n-=1
    if n == 0:
        break
print(fact)
