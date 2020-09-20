def perfect(start,end):
    for n in range(start,end+1):
        sum=0
        for x in range(1,n):
            if n%x == 0:
                sum+=x
        if sum == n:
            print(n,end=", ")

n,m=[int(n) for n in input("Enter Number From and To u wanna to check the Perfect Number \nAnd split them by \"-\":\n").split("-")]
perfect(n,m)
