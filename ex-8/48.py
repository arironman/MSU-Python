num = int(input("Enter the Number: "))
lst=[]
for x in range(1,num):
    if num%x == 0:
        lst.append(x)
sum=0
for x in lst:
    sum+=x
if sum == num:
    print(f"{num} is a Perfect Number: ")

else:
    print(f"{num} is not a Perfect Number: ")
