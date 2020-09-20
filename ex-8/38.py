#here i use split function for practice and revise
num1,num2=[int(num1) for num1 in input("Enter Number Number 1 and Number 2 and Split thm by \",\": ").split(",")]
#using for loop
print("Using for loop: ")
for x in range(1,num1+1):
    if num1%x == 0 and num2%x == 0:
        hcf=x

print(f"HCF of {num1} and {num2} is: {hcf}")



#Using While Loop
print("Using While loop: ")
x=1
while x<=num1:
    if num1%x == 0 and num2%x == 0:
        hcf=x
    x+=1
print(f"HCF of {num1} amd {num2} are: {hcf}")
