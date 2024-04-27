Practical = {"Name": "Vishal", "Surname" : "Mahajan"}

#1. Keys : Return the keys of the dictionary
print("Keys in Dictionary are",Practical.keys())

#2. Values : Return the values of the dictionary
print("values in Dictionary are",Practical.values())

#3. update : Update the dictionary with the specified key-value pairs
Practical.update({"Class" : "SE-IT-A3"})
print(Practical)

#4. get : Return the value of the specified key
print("Name is ",Practical.get("Name"))

#5. pop : Remove the element with the specified key
Practical.pop("Class")
print("After Poping Class,Dicitonary is",Practical)

#6. popitem() : Remove the last inserted key-value pair
Practical.popitem()
print("After poping item,Dictionary is",Practical)

#7. setdefault : Return the value of the specified key. If the key does not exist: insert the key, with the specified value
Practical.setdefault("Surname","Mahajan")
print("After setting default,Dictinoray is",Practical)

#8. copy : Return a copy of the dictionary
CopiedPractical = Practical.copy()
print("Copied Dictionary is",CopiedPractical)

#9. items : Return a list containing a tuple for each key value pair
Practical.items()
print(Practical.items())

#10. clear : Remove all elements from the dictionary
print(Practical.clear())