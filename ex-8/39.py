num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))
if num1>num2:
    num=num2
else:
    num=num1
for x in range(1,num+1):
    if num1%x == 0 and num2%x == 0:
        hcf=x
n1=num1
n2=num2
lcm=hcf*(n1/hcf)*(n2/hcf)
print(f"LCM of {num1} and {num2} is {lcm}")
