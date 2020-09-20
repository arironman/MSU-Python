n=int(input("Enter Number of Rows u wanna to print: "))
x=input("Enter the character: ")
for i in range(n,0,-1):
    for j in range(0,i):
        print(x,end=" ")
    print("")
