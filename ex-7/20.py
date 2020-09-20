#isalpha() and isnumeric() is methord which return true if the given charactre
#is alphabet and number respictively
ch=input("Enter a Character: ")
if ch.isalpha():
    print(f"{ch} is a  alphabet")
elif ch.isnumeric():
    print(f"{ch} is a Digit")
else:
    print(f"{ch} is a special Character")
