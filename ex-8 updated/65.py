n=int(input("Enter the Number: "))
m=int(n/2)
val=0
for x in range(2,m+1):
    if n%x == 0:
        val=1
        break
if val == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")
