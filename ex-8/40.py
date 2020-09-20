num=int(input("Enter the Number: "))
print(" Using for loop")
for x in range(2,num):
    if num%x == 0:
        print("Number is not Prime")
        break
if x == num-1:
    print("Number is Prime")



#i can also do it by using while loop
