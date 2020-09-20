n=int(input("Enter Number of Rows u wanna to print: "))
x=input("Enter the character: ")
space=0
for i in range(n,0,-1):
    print(" "*space,end=" ")
    for j in range(0,i):
        print(x,end=" ")
    print("")
    space+=2


