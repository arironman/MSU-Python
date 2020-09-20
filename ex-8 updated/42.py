print("Enter 10 Numbers: ")
list=[]
sum=0
for x in range(0,10):
    list.append(int(input()))
    sum+=list[x]
print(sum/10)
