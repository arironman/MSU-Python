def hcf(x,y):
    for i in range(1,x+1):
        if x%i == 0 and y%i == 0:
            num=i
    return num
x=int(input("Enter Smaller Number: "))
y=int(input("Enter another Number: "))
print(hcf(x,y))
