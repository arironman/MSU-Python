m=int(input("Enter the starting range: "))
n=int(input("Enter the ending Number: "))

for x in range(m,n+1):
    if x%2 == 0:
        print(f"Even Number: {x}")
    else:
        print(f"Odd Number: {x}")
