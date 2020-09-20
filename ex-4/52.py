import intro #Use to style and to introduce about the developer of the program


from math import sqrt
x,y,z=[int(x) for x in input("Enter ths sides of Triangle: ").split(",")]
s=(x+y+z)/2
print("Area of the Triangle is: ", sqrt(s*(s-x)*(s-y)*(s-z)))


import end #Use to give style while ending the program
