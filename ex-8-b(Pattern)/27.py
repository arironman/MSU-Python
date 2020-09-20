n=int(input("Enter Number of rows: "))
x=input("Enter which character which u wanna to print: ")
space=(n-1)*2
for i in range(1,n+1):
    print(" "*space,end=" ")
    for j in range(1,2*i):
        print(x,end=" ")
    space-=2
    print("")
