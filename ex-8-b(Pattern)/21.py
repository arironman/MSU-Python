n=int(input("Enter Number of rows u wanna to print: "))
space=2*(n-1)
for i in range(1,n+1):
    print(" "*space,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    space-=2
    print("")
