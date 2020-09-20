#ASCII=American Standard Code for Information Interchange
#ASCII code start from 0 and end at 255

#chr(ascii code) function used to convert ASCII Code to respective character
#ord("Character") function used to convert Character to respective ASCII code


for x in range(0,256):
    print(f"ASCII code of {chr(x)} is {x}")
