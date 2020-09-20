n=int(input("Enter no of rows: "))
val=1
space=(n-1)*2
for i in range(1,n+1):
    print(" "*space, end="")
    for x in range(val,0,-1):
        print(x,end=" ")
    for j in range (x+1,val+1):
        print(j,end=" ")
    val+=1
    print("")
    space-=2


        
