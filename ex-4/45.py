import intro #Use to style and to introduce about the developer of the program


x=input("Enter your name , Age and Salary Respictively ")
y=int(input())
z=float(input())
i=int(input("Ways of Seperation\n Press 1 if You wanna to seperate by \",\" \n Press 2 if you wanna to seperate by tab \n Press 3 if you wanna to seperate it by new line \n Press 4 if you wanna to seperate it by \":\"\n"))
if i == 1:
    print("Name: %s , Age: %i , Salary: %5.2f " %(x,y,z))
elif i == 2:
    print("Name: %s \t Age: %i \t Salary: %5.2f " %(x,y,z))
elif i == 3:
    print("Name: %s \n Age: %i \n Salary: %5.2f " %(x,y,z))
elif i == 4:
    print("Name: %s : Age: %i : Salary: %5.2f " %(x,y,z))
else :
    print("Wrong input \n Try Again !!!")


import end #Use to give style while ending the program
