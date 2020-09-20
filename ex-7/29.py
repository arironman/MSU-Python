#here we also use dictionary instead of many if statements
grade={9:"Grade A",
       8:"Grade B",
       7:"Grade C",
       6:"Grade D",
       4:"Grade E"}

mark=int(input("Emter your Marks: "))
x=mark//10      #here is the reason whi i take 9 instead of 90 and so on

if x>4:
    print(f"your Grade is {grade[x]}")
else:
    print("your grade is garde F")
