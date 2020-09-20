n=int(input("How many rows u wanna to print: "))
x=input("Enter the Character which u wanna to print: ")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(x,end=" ")
    print("")
