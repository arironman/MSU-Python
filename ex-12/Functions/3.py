def comparision(m,n):
    if m>n:
        print(f"{m} is Maximum Number and {n} is Minimum Number")
    elif m<n:
        print(f"{n} is Maximum Number and {m} is Maximum Number")
    else:
        print(f"Both the Numbers are Equal")
x,y=[int(x) for x in input("Write 2 Numbers and split them by space: ").split()]
comparision(x,y)
