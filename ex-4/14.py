import intro #Use to style and to introduce about the developer of the program


print(" Press 1 to convert centigrate to Fahrenheit\nPress 2 to convert Fahrenheit to centigrade ")
x=int(input())
if x==1:
    c=int(input("Enter value in Centigrate"))
    f=c*1.8 + 32
    print("Temperature in Fahreinheit is ",f)

elif x==2:
    f=int(input("Enter value in fahreinheit "))
    c=(f-32)/1.8
    print("Temperature in Celcius is ",c)
else:
    print("Wrong Input \n Try Again!")


import end #Use to give style while ending the program
