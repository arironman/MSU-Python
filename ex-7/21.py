x=int(input("Enter Week Number(Consider Sunday =0): "))
# we use dictonary instead of loop 
week={0:"Sunday",
      1:"Monday",
      2:"Tuesday",
      3:"Wednesday",
      4:"Thursday",
      5:"Friday",
      6:"Saturday"}
print(f"week number {x} is {week[x]}")
