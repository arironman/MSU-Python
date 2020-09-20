import intro #Use to style and to introduce about the developer of the program


x,y=[int(x) for x in input("Enter x and y respictively ").split(",")]
x=x+y
y=x-y
x=x-y
#or we can also do it by x,y=y,x
print("After Swapping \n x = ",x," and y = ",y)


import end #Use to give style while ending the program
