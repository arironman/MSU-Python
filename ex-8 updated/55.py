def product(n):
    p=1
    while n != 0:
        tmp=n%10
        n=n//10
        p*=tmp
    return p
print(product(int(input("Enter  a Number: "))))
