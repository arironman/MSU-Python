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
def fact(n):
    m=int(n/2)
    for x in range(1,m+1):
        if n%x == 0:
            if prime(x) == None:
                pass
            else:
                print(prime(x))

fact(int(input("Enter a Number: ")))
