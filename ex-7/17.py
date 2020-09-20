#our Approach to ba a smart programmer so we don't use our memory 
#we don't use a=97 like that we don't take any thing ahd gert the result
A=ord('A')  #here in A we get the ASCII value of A
Z=ord('Z')    #same as above
a=ord('a')
z=ord('z')
x=input("Enter a Character: ")
ch=ord(x)
if ch>=a and ch<=z:
    print(f"{chr(ch)} is Lower Case character")
elif ch>=A and ch<=Z:
    print(f"{chr(ch)} is Upper Case character")
else:
    print(f"{chr(ch)} is not a Alphabet")

    
