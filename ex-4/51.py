import intro #Use to style and to introduce about the developer of the program


i=int(input(" Press 1 to convert km to miles\n Press 2 to convert miles to km\n"))
if i == 1:
    km=float(input("Enter the distance in kilometer: "))
    print("Distance in miles is: ",km*0.62137)
elif i == 2:
    mile=float(input("Enter Distance in miles: "))
    print("Distance in kilometer: ", mile/ 0.62137)


import end #Use to give style while ending the program
