#Here i am trying my logic it is right but may be any more relivant technique
#is present or not
n=int(input("Enter a Number: "))
#For First digit
num=n    #here i store origina;l value into an variable
        #because we need it again
count=0
while num>10:
    num=num//10
    count+=1
print(f"First Digit is {num}")


num2=n

#For last Digit
last=num2%10
print(f"Last Digit is {last}")


#to replace first and Last Digit
x=(num*(10**count))+last
y=(last*(10**count))+num
final=n-x+y
print(f"Replace of First and last Digit {final}")

