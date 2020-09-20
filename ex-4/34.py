import intro #Use to style and to introduce about the developer of the program


x=int(input(" Press 1 to convert Binary to Decimal \n Press 2 to convert Octal to Decimal \n Press 3 to convert Hexadecimal to Decimal"))
if x == 1 :
    a=input("Enter Number in binary ")
    print("Number in Decimal is " ,int(a,2))
elif x == 2 :
    a=input("Enter Number in octal ")
    print("Number in Decimal is " ,int(a,8))
elif x == 1 :
    a=input("Enter Number in Hexadecimal ")
    print("Number in Decimal is " ,int(a,16))
else:
    print(" You have written wrong value\n Try again !!!")


import end #Use to give style while ending the program
