year =int(input("Enter a Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is Not a leap Year")
    else:
        print(f"{year} is a Leap Year")
else:
    print("Year is Not a Leap Year")
