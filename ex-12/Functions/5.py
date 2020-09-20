def prime(n):
    count=0
    for x in range(2,n):
        if n%x == 0:
           count=1
           break
    if count == 0:
        return True
    else:
        return False





def armstrong(num):
    n=num
    sum=0
    while n != 0:
        temp=n%10
        n=n//10
        sum+=(temp**3)
    if sum == num:
        return True
    else:
        return False




def perfect(n):
    sum=0
    for x in range(1,n):
        if n%x == 0:
            sum+=x
    if sum == n:
        return True
    else:
        return False


    

def prop(n):
    print("Press 1 if u wanna check prime Number:\nPress 2 if u wanna to check Armstrong Number:\nPress 3 if u wanna to check Perfect Number: \n")
    i=int(input())
    if i == 1:
        if prime(n):
            print(f"{n} is a Prime Number")
        else:
            print(f"{n} is not a Prime Number")
    elif i == 2:
        if armstrong(n):
            print(f"{n} is a Armstrong Number")
        else:
            print(f"{n} is not a Armstrong Number")
    elif i == 3:
        if perfect(n):
            print(f"{n} is a Perect Number")
        else:
            print(f"{n} is not a Perfct Number")
    else:
        print("Sorry u press wrong Number ")
    x=int(input("Press 1 if u wanna to do it again otherwise press 0: "))
    if x == 1:
        return prop(n)
    
n=int(input("Enter the Number: "))
prop(n)
