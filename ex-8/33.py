#here i make a dictionary to store word withtheir respective number
word={0:"Zero",
      1:"One",
      2:"Two",
      3:"Three",
      4:"Four",
      5:"Five",
      6:"Six",
      7:"Seven",
      8:"Eight",
      9:"Nine"}
num=int(input("Enter a Number: "))
temp=num
lst=[]
while temp != 0:
    mod=temp%10
    lst.append(mod)
    temp=temp//10
lst.reverse()
for x in lst:
    print(word[x],end=" ")
