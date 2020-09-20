def armstrong(start,end):
    for x in range(start,end+1):
        n=x
        sum=0
        while n != 0:
            temp=n%10
            n=n//10
            sum+=(temp**3)
        if sum == x:
            print(x,end=", ")
n,m=[int(n) for n in input("Enter Number From and To u wanna to check the armstrong Number \nAnd split them by \"-\":\n").split("-")]
armstrong(n,m)
