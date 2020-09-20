def hcf(x,y):
    for i in range(1,x+1):
        if x%i == 0 and y%i == 0:
            num=i
    return num

def lcm(x,y):
    num=hcf(x,y)
    x=x/num
    y=y/num
    return x*y*num



x=int(input("Enter Smaller Number: "))
y=int(input("Enter another Number: "))
print(lcm(x,y))
