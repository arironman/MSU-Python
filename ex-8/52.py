n=int(input("Enter till how many Numbers u wanna to print fibonaaci series: "))
temp=0
for x in range(0,n):
    if x <= 1:
        print(x,end=" ")
        temp2=temp
        temp=x
    else:
        next=temp+temp2
        temp2=temp
        temp=next
        print(next,end=" ")
        
