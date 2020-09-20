import intro #Use to style and to introduce about the developer of the program


x,y=[int(x) for x in input("Enter Number 1 and Number 2 respictively and split them by space: ").split()]
if x>y:
    print("Number 1 is Greater than Number 2:")
elif y>x:
    print("Number 2 is Greater than Number 1:")
else:
    print("Both Number contaun same value:")


import end #Use to give style while ending the program
