thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
      print(x)

print("banana" in thisset)

thisset.add("orange")
print(thisset)

print(len(thisset))

thisset.remove("banana")
print(thisset)

thisset.pop()
print(thisset)

thisset.clear()
print(thisset)

del thisset
print(thisset)
