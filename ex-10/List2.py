list1=[1,2,3,4,5,6]


#Delete an item from the List
list1.pop()
print(list1)


#Remove Element at odd Place
for i in range(0,len(list1)):
    if i%2 != 0:
        list1.pop(i)
print(list1)

#Remove Element at Even Places
for i in range(0,len(list1)-1):
    if i%2 == 0:
        list1.pop(i)
print(list1)



#remove all the elements of the List
list1=[1,2,3,4,5]
print(list1)
list1.clear()
print(list1)




#Detete the definion of the list and verify it
list1=[1,2,3,4,5]
del list1
try:
    print(list1)
except:
    print("Sorry List is not defined ")



#Create a nested list consisting of various elements along with one or two lists.
list1=[1,2,[67,85],["abc","xyz"]]
print(list1)





#Clone alist into another list.
list2=list1
print(list2)
