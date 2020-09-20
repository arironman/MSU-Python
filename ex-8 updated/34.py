def leap(x):
    
    if x%4 == 0:
        if x%100 == 0 and x%400 == 0:
            return True
        elif x%100 == 0 and x%400 != 0:
            return False
        else:
            return True
    else:
        return False



n=int(input("Enter year range starting from: "))
m=int(input("Enter till where u wanna to find leap year: "))
count=0
for x in range(n,m+1):
    if leap(x):
        count+=1
print(count)
