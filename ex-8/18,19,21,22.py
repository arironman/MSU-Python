n=int(input("Enter range"))

print("\t Even Nuimber")
for x in range(1,n+1):
    if x%2 == 0:
        print(x, end=" ")




print("\n\t Odd Number")
for x in range(1,n+1):
    if x%2 != 0:
        print(x,end=" ")
    
