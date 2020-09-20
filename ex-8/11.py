year1 =int(input("Enter a Year from: "))
year2=int(input("Enter year to: "))
for year in range(year1,year2+1):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year)
        
        else:
            print(year)
