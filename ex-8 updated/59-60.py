n=int(input("Enter a Number: "))
def frequency(n):
    list=[]
    while n != 0:
        list.append(n%10)
        n=n//10
    print(f"Frequency of:\n 0: {list.count(0)}\n 1: {list.count(1)}\n 2: {list.count(2)}\n 3: {list.count(3)}\n 4: {list.count(4)}\n 5: {list.count(5)}\n 6: {list.count(6)}\n 7: {list.count(7)}\n 8: {list.count(8)}\n 9: {list.count(9)}\n")
frequency(n)
