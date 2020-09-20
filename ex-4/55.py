import intro #Use to style and to introduce about the developer of the program


y=1
while y == 1:
    i=int(input("\t\t\t Welcome to Converter Calculator\nPress \t\t from \t\t to \n1\t\t Meters \t Feet\n2 \t\t Feet \t\t meter \n3 \t\t inches \t cm\n4 \t\t cm \t\t inches \n5 \t\t mm  \t\t inches \n6 \t\t inches \t mm \n7 \t\t inches \t feet \n8 \t\t feet \t\t inches\n"))

    if i == 1:
        x=float(input("Enter the value in Meters: "))
        print(x," Meters is ", x*3.2808 ," Feet ")
    elif i == 2:
        x=float(input("Enter the value in Feet: "))
        print(x," Feet is ", x/ 3.2808 ," Meter")

    elif i == 3:
        x=float(input("Enter the value in Inches: "))
        print(x," Inches is ", x/ 0.39370 ," Centimeter")

    elif i == 4:
        x=float(input("Enter the value in Centimeter: "))
        print(x," Centimeter is ", x*0.39370 ," Inches")

    elif i == 5:
        x=float(input("Enter the value in Millimeter: "))
        print(x," Millimeter is ", x*0.039370 ," Inches")

    elif i == 6:
        x=float(input("Enter the value in Inches"))
        print(x," Inches is ", x/ 0.039370 ," Millimeter")

    elif i == 7:
        x=float(input("Enter the value in Inches"))
        print(x," Inches is ", x*0.083333 ," Feet")

    elif i == 8:
        x=float(input("Enter the value in Feet: "))
        print(x," Feet is ", x*12.000 ," Inches")
    y=int(input("Press 1 if you wanna to continue otherwise Press 2 to end the Program."))


import end #Use to give style while ending the program
