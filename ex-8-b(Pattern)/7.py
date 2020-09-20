n=int(input("Enter Number of rows u want: "))
m=int(input("Enter Number of Columns u want: "))
x=1
for i in range(0,n):
    for j in range(0,m):
        print(x,end=" ")
        if x<10:
            print(" ",end="")
        x+=1
    print("")
