side=[]
for x in range(0,3):
    a=int(input(f"Enter side{x+1}: "))
    side.append(a)
if side[0]==side[1]==side[2]:
    print("Triangle is Equivalent")
elif side[0]==side[1] or side[1]==side[2] or side[0]==side[2]:
    print("Triangle is isosceles")
else:
    print("Triangle is scalar")
