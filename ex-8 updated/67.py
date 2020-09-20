def prime(n):
    m=int(n/2)
    val=0
    for x in range(2,m+1):
        if n%x == 0:
            val=1
            break
    if val == 0:
        return n
    else:
        pass

m=int(input("Till where u wanna to check: "))
for i in range(1,m+1):
    if prime(i) == None:
        pass
    else:
        print(prime(i))
