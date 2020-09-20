#List created
list1=[1,2,3,4]


#Iterated Over List
for x in list1:
    print(x)


#Concatenation 2 List
list2=[5,6,7,8]
list3=list1+list2
print(list3)



#Multiplication of a List by a number
list3=[]
for i in range(0,len(list1)):
    list3.append(list1[i]*5)
print(list3)

#or we can also do
#list3=[i*5 for i in list]




