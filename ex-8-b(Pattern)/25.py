n=int(input("Enter Number of rows: "))
space=(n-1)*2
for i in range(1,n+1):
    print(" "*space,end=" ")
    for j in range(1,i+1):
       print(i,end=" ")
    print("")
    space-=1
