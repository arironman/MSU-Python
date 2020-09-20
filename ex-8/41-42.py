start = int(input("Enter from where u wanna to start the interval: "))
end = int(input("Enter till where u want to end the interval: "))
lst=[]
for x in range(start,end+1):
    var=2
    for i in range(2,x):
        if x%i == 0:
            var=1
            break
    if var == 2:
        lst.append(x)
print("The prime Number b/w {start} and {end} is :",end=" ")
for x in lst:
    print(x,end=" ")
