#Perform various slicing operations on a print string
str = "The Maharaja Sayajirao University of Baroda, Vadodara"

#code                 Output

print(str)      #The Maharaja Sayajirao University of Baroda, Vadodara
print(str[6])   #h
print(str[-2])  #r
print(str[-10]) #,
print(str[0:6]) #The Ma
print(str[1:6]) #he Ma
print(str[6:10])    #hara
print(str[:])   #The Maharaja Sayajirao University of Baroda, Vadodara
print(str[::])  #The Maharaja Sayajirao University of Baroda, Vadodara
print(str[::-1])    #aradodaV ,adoraB fo ytisrevinU oarijayaS ajarahaM ehT
print(str[:10]) #The Mahara
print(str[::2]) #TeMhrj aaia nvriyo aoa aoaa
print(str[0::1])    #The Maharaja Sayajirao University of Baroda, Vadodara
print(str[2:13:4])  #ehj






#in and not in operators
print("\n\n\n\nPrint use of in operator:")
if "Univ" in str:
    print(f"The Univ is present in {str}")

print("Using Not in operator: ")
if "Guj" not in str:
    print(f"Guj is not Preaent in {str}")
    
