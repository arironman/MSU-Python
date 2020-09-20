import intro #Use to style and to introduce about the developer of the program


z=[]
print("Enter name age and Percentage: ")
for x in range(0,7):
    z.insert(x,input())
    if x!= 0:
        z[x]=eval(z[x])
    if x == 6:
        break
x=0
print("Name: %20s , Age: %-20i , \n Percentage: %i \t %i \t %i \t %i \t %i  "%(z[0],z[1],z[2],z[3],z[4],z[5],z[6]))
 


import end #Use to give style while ending the program
