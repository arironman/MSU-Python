def leap(x):
    if x%4 == 0:
        if x%100 == 0 and x%400 == 0:
            print(x)
        elif x%100 == 0 and x%400 != 0:
            pass
        else:
            print(x)
    else:
        pass



n=int(input("Enter year range starting from: "))
m=int(input("Enter till where u wanna to find leap year: "))
for x in range(n,m+1):
    leap(x)
