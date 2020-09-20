import intro #Use to style and to introduce about the developer of the program


tup1 = ('a' , 'bc' ,78, 1.23 , 'Python', 3.14 , 8977)
tup2= 'd' , 45
print(tup1)
print(tup1[0])
print(tup1[2])
print(tup1[1:3])
print(tup1[2:])
print(tup1[-2])
print(tup1*2)
print(tup1+tup2)
tup1[0]='z';        #it will not happen becuse it is touple but this code show no error in list because elements of tuple are fixed
print(tup1)


import end #Use to give style while ending the program
