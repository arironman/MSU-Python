n=int(input("Enter teh Last Term of the series: "))
sum=1
for i in range(2,n+1):
    sum=sum+(i**(2/i))
print(sum)
