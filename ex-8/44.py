num= int(input("Enter the Number: "))
n=num
lst=[]
for x in range(2,num):
    var=2
    for i in range(2,x):
        if x%i == 0:
            var=1
            break
    if var == 2 and num%x == 0:
        lst.append(x)
for x in lst:
    print(x,end=" ")
