def prime(start,end):
    for x in range(start,end+1):
        count=0
        for i in range(2,x):
            if x%i == 0:
                count=1
        if count == 0:
            print(x,end=" , ")


n,m=[int(n) for n in input("Enter Number from and Number to u wanna to print prime Number\nSplit them by \"-\": \n").split("-")]
prime(n,m)
