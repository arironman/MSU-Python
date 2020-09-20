# formula= -b+-[((b^2)-4ac)^(1/2)]/2a
a,b,c=[int(a) for a in input("Enter a a,b and c respictively \nand split them by\",\": ").split(",")]
z=(b**2)-(4*a*c)
y=z/(2*a)
print(f"Root of the Quardatic Equation are : {-b+y} and {-b-y}")
