#in loops if u get confused then take eg on paper and find output by own
#and Understand every logic
x= int(input("Enter Number: "))
count=0
while x>0:
    x=x//10
    count=count+1

print(f"Number of Digits is {count}")
    
