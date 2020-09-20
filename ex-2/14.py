import intro #Use to style and to introduce about the developer of the program


x=int(input("Enter the Number of items you wanna to Display in a list "))
name=[]
qty=[]
price=[]
total=0
for y in range (0,x):
 print("Details of Item Number ",y+1)   
 a=input("Name of item ")
 name.insert(y,a)
 b=int(input("Quantity of item "))
 qty.insert(y,b)
 c= int(input("Price of itme "))
 price.insert(y,c)
print("#"*15,"B I L L", "#"*15)
print("Serial No. \t \t Item Name \t \t Item Quantity \t \t Item Price")
for y in range(0,x):
 print(y+1,"\t \t \t",name[y],"\t \t \t",qty[y],"\t \t \t",price[y])
 total+=price[y]

print("*"*40)
print("Total Amount to be paid \t \t \t \t \t \t" ,total )

print("*"*40)


import end #Use to give style while ending the program
