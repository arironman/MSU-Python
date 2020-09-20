#if a Number has n digits/order
#then the sum of each digit to the power of order , if this is eqaul to
#actul Number then the Number is armstrong
#0,1,153,370,371and 407 are only armstrong number present
#so for making prog simple we will take n=3(order)
num = int(input("Enter the Number: "))
n=num
add=0
for x in range(0,3): 
    temp=n%10
    n=n//10
    add=add+(temp**3)
if add == num:
    print(f"{num} is Armstrong Number")
else:
    print(f"{num} is not a Armstrong Number")
