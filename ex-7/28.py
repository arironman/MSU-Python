sp=int(input("Enter Selling Price: "))
cp=int(input("Enter Cost Price: "))
x=sp-cp
if x>0:
    print(f"Profit of {x}")
else:
    print(f"loss of {(-1)*x}")
