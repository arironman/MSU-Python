import intro #Use to style and to introduce about the developer of the program


print(" Press 1 to convert kelvin to Fahrenheit\nPress 2 to convert Fahrenheit to kelvin ")
x=int(input())
if x==1:
    k=int(input("Enter value in kelvin"))
    f=(k-273.15)*1.8 + 32
    print("Temperature in Fahreinheit is ",f)

elif x==2:
    f=int(input("Enter value in fahreinheit "))
    k=((f-32)/1.8) + 273.15
    print("Temperature in kelvin is ",k)
else:
    print("Wrong Input \n Try Again!")


import end #Use to give style while ending the program

