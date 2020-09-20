n=int(input("Till where u wanna to write number: "))
n=n//10
for i in range(1,11):
    num=i
    for j in range(1,n+1):
        print(num,end="  ")
        if num < 10:
            print(" ",end="")
        num+=10
    print("")
