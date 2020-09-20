#in ever piece of code we try to use this string as possible
string="Anurag Rai"





#iterate Over String
#Using Slicing methord may be
print("This is may be known as slicing methord:")
print(string[::])


#Using for loop
print("Iteration using for loop: ")
for x in range(0,len(string)):
    print(string[x],end="")



#Iterate Over String and Display its Elements along with its index String
print("\n \nIterate Over String and Display its Elements along with its index String")
for x in range(0,len(string)):
    print(f"{string[x]} has index Number {x}")




#Concatenate 2 strings
print("\n\nConcatenate two String:")
str1="Anurag "
str2="Rai"
print(f"Concatenate str1 and str2 is: {str1+str2} ")




#Concatenate 4  Strings
print("\n\nConcatenate 4  Strings")
str1="abcd"
str2="efgh"
str3="ijkl"
str4="mnop"
print(f"Concatenate of 4 string is: {str1+str2+str3+str4}")
#This can also be done by using % operator, fstring and format function



#Concatenate string with Number
str1= "Anurag"
num=15
#Using % Operator
print("Concatenate by using % operator:")
print("Concanate of two string are: %s%i "%(str1,num))
#Using fstring
print("Concatenate by using fstring:")
print(f"Concanate of two string are: {str1}{num} ")
#Using format function
print("Concatenate by using format function:")
print("Concanate of two string are: {}{} ".format(str1,num))





#Multiply string with a string is Impossible
#May be it is Multiply a string with a Integer
str1="Ironman"
num=5
print("Multiplication of string and Integer are:")
print(str1*num,end=" ")





#Convert a number, list, tuple into string.
#Number to string
print("\n\n\nNumber to String:")
num=1234
str1=str(num)       #This is Known as type casting
print(f"{str1} and it is of type {type(str1)}")

#List to string
print("\nList to String")
lst=["Anurag","15","rai"]
#Using iteration using for loop
print("By Iteration using for loop: ")
str1=""
for x in lst:
    str1+=x
print(f"{str1} and it is of type {type(str1)}")

#Using iteration using for loop may be little mistake somewhere here
print("By Iteration using for loop and using join function: ")
str1=""
for x in lst:
    str1+=str("".join(x))
print(f"{str1} and it is of type {type(str1)}")
#it can also be done by map function but till now not in syllabus





#Print a raw string.
#It can be done by using "r" or "R" before writing the string
#And it also can be done by using backslash(\) before special character like(\n,\t,'," and so on)
print("\n\nPython Raw String:")
print(r"This is done by using raw string \n ")
print("This can be done by using backslash(\) \\n")






#Print a Unicode string
#No idea





#Demonstrate that a string is immutable.
print("\n\nProgram to show that string is immutable: ")
str="Anurag"
try:
    str[0]="Z"
    print(str)
except:
    print("string is immutable")
    print






#Print the character of the string available at index 0 and index 3
string="Anurag Rai"
print("\n\nPrint the Character is available at index 0 and 3 : ")
print(f"Character Present at index 0 is {string[0]}")
print(f"Character Present at teh index 3 is {string[3]} ")





#Delete a string
print("\n\nDelete a string")
string="Anurag"
print("Using Del keyword:")
del string
try:
    print(f"The string is: {string}")
except:
    print("The string is Deleted")



