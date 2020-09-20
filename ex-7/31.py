x=int(input("Enter Elctricity units: "))
if x>50:
    amount=50*0.5
    x=x-50
    if x>100:
        amount=amount+(100*0.75)
        x=x-100
        if x>100:
            amount=amount+(100*1.20)
            x=x-100
            if x>0:
                amount=amount+(x*1.5)
        else:
            amount=amount+(x*1.20)
    else:
        amount=amount+(x*0.75)
else:
    amount=x*0.5
print(f"Total amount will be {amount} \nAnd by including Additional subcharge it became Rs {amount + (amount/5)} ")

