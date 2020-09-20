n=int(input("Till where u wanna to print table: "))
for i in range(1,11):
    for j in range(1,n+1):
        print(j*i,end="  ")
        if j*i < 10:
            print(" ",end="")
    print("")
