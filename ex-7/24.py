a=int(input("Enter angle 1: "))
b=int(input("Enter angle 2: "))
c=int(input("Enter angle 3: "))
if a == 0 or b == 0 or c == 0:
    print("Sorry This not a Traingle because any of angle is equal to 0 degree")
else:
    if (a+b+c) ==  180:
        print("This is A triangel")
    else:
        print("This is not a triangle because the su of angles is nor 180 degree.")
                             
