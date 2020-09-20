n=int(input("Enter Number of Rows: "))
x=input("Enter the character which u wanna to print: ")
space=2*(n-1)
for i in range(0,n):
    print(" "*space,end=" ")
    for j in range(0,i):
        print(x,end=" ")
    print("")
    space-=2
