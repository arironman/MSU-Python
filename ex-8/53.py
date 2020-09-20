n=int(input("Enter under how many Numbers u wanna to print fibonaaci series: "))
temp=0
for x in range(0,n-1):
    if x <= 1:
        print(x,end=" ")
        temp2=temp
        temp=x
    else:
        next=temp+temp2
        temp2=temp
        temp=next
        print(next,end=" ")
        
