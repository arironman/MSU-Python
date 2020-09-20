n=int(input("Enter Number of rows u wanna to print: "))
m=int(input("Enter Number of Columns u wanna to print: "))
x=input("Enter the character which u wanna to print: ")
for i in range(0,n):
    for j in range(0,m):
        if i == n-1 or j == 0 or i == 0 or j == m-1:
            print(x,end=" ")
        else:
            print(" ", end=" ")
    print("")    
