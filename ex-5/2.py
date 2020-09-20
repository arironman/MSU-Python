import intro #Use to style and to introduce about the developer of the program


x,y,z=[int(x) for x in input("Enter the sides of Triangle and split them by giving space: ").split()]
s=(x+y+z)/2
from math import sqrt
print("Area of Triangle is: ", sqrt(s*(s-x)*(s-y)*(s-z)) )


import end #Use to give style while ending the program
