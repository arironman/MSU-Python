start = int(input("From where u wanna to check the perfect Number: "))
end = int(input("Till where u wanna to check the perfect Number: "))


strong=[]
for num in range(start,end+1):
    n=num
    x=1
    sum=0
    lst=[]
    while x == 1:
        mod=n%10
        lst.append(mod)
        n=n//10
        if n == 0:
            break
    for x in lst:
        multi=1
        for i in range(1,x+1):
            multi= multi*i
        sum+=multi

    if sum == num:
        strong.append(num)
   
print("The list of strong number b/w {start} and {end} is: ",end="")
for x in strong:
    print(x,end=" ")
