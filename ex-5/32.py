import intro #Use to style and to introduce about the developer of the program


from math import pi,pow
x=int(input("Enter the radius of the circle: "))
print("Area of the Circle is: ",pi*pow(x,2))
area=pi*pow(x,2)
print("Area upto 2 digits after decimal: {:.2f}".format(area))


import end #Use to give style while ending the program
