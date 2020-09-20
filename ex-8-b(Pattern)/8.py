n=int(input("Enter Number of rows u wanna to print: "))
val=1
for i in range(0,n*5):
    print(val,end=" ")

    if val < 10:
        print(" ",end="")
    if val%5 == 0:
        print("")
    val+=1
    
