#Here We use List but in Smarter way
x= int(input("Enter Month Number(jan=1): "))
month=[4,6,9,10]
if x in month:
    print(f"{x} has 30 days")
elif x  == 2:
    print(f"{x} has 28/29 days")
else:
    print(f"{x} has 31 days")
        
