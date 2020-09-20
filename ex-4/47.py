import intro #Use to style and to introduce about the developer of the program


n = int(input("Enter number of elements : ")) 
i=int(input(" Press 1 for using map funcion \n Press 2 for using for loop methord \n"))

if i==1:
    
    # Below line read inputs from user using map() function  
    a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
  
    print("\nList is - ", a)

  #or
elif i == 2:
    lst=[]
    for x in range(0,n):
        lst.insert(x,eval(input("Enter value %i in List:" %(x+1))))
    print("List is: ",lst)
     
     


import end #Use to give style while ending the program
