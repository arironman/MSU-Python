n=int(input("Enter teh Last Term of the series: "))
sum=0
for i in range(1,n+1):
    sum=sum+(i/i+1)
print(sum)
