#Pattern of 1 and 0 in alternate columns
n=int(input("Enter Number of rows: "))
m=int(input("Enter Number of columns: "))
for i in range(0,n):
    for j in range(0,m):
        if j%2 == 0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print("")
