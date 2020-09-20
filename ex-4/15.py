import intro #Use to style and to introduce about the developer of the program


print(" Press 1 to convert centigrate to kelvin\nPress 2 to convert kelvin to centigrade ")
x=int(input())
if x==1:
    c=float(input("Enter value in Centigrate"))
    k=c+ 273.15
    print("Temperature in kelvin is ",k)

elif x==2:
    k=float(input("Enter value in kelvin "))
    c=k-273.15
    print("Temperature in Celcius is ",c)
else:
    print("Wrong Input \n Try Again!")


import end #Use to give style while ending the program
