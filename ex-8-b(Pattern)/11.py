n=int(input("Enter Number of Rows: "))
m=int(input("Enter Number of Columns: "))
x=input("Enter Character which u wanna to print: ")
space=m-1
for i in range(0,n):
    print(" "*space,end=" ")
    for j in range(0,m):
        print(x,end=" ")
    print("")
    space-=1
