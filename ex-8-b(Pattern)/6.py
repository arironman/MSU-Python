n=int(input("Enter Number of rows: "))
m=int(input("Enter Number of Columns: "))
val=1
for i in range(0,n):
    temp=0
    for j in range(0,m):
        print(val+temp,end=" ")
        if val+temp < 10:
            print(" ",end="")
        temp+=1
    val+=1
    print("")    
