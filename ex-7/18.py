# Palindrome Means if we reverse the string is look same as before
#like rar
string=input("Enter a String: ")
rev=string[::-1]
if string == rev:
    print("It is Palindrome:")
else:
    print("The Given string is Not Palindrome")
