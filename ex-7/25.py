
side=[]
for x in range(0,3):
    a=int(input(f"Enter side{x+1}: "))
    side.append(a)
if side[2]+side[1]>side[0] and side[0]+side[2]>side[1] and side[0]+side[1]>side[2]:
    print("This is a Prefect Triangle")
else:
    print("Thius is Not a triangle")
    
