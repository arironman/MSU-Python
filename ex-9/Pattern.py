#Pattern 1
print("Pattern 1")
num=int(input("Enter how many rows u wanna sir: "))
for x in range(1,num+1):
    print("&"*x)



#Pattern 2
print("\n\n\nPattern 2")
num=int(input("Enter how many rows u wanna sir: "))
for x in range(num,0,-1):
    print("*"*x)



#Pattern 3
print("\n\n\nPattern 3")
num=int(input("Enter how many rows u wanna sir: "))
for x in range(1,num+1):
    print("*"*x)
for x in range(num-1,0,-1):
    print("*"*x)
