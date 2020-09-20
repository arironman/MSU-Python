from math import log
def prop(n):
    print(f"{n};SQUARE:{n*n};CUBE:{n*n*n};LOG:{log(n)};SQUAREROOT:{n**(1/2)};CUBEROOT:{n**(1/3)};")
for x in range(1,101):
        prop(x)
    
