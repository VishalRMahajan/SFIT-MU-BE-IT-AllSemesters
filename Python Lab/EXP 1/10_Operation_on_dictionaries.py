#Python Dictionaries

#Three ways to create Dictionaries
#Type 1
type1={"Name":"Vishal","Surname":"Mahajan","Age":"Eigtheen"}
print(type(type1))
print("The original Dicitonary is ",type1)

#Type2
type2= dict ({63:"Vishal",64:"Shubham"})
print("Dicitonary with use of dict() is ",type2)
print(type(type2))

#Type3
type3= dict([(63,"Vishal"),(64,"Shubham")])
print(type(type3))
print("Dicitonary with each item as a pair ",type3)

#Change the Values
type1["Age"]=20
print("The updated Dicitonary is ",type1)


#Printing all keys
for keys in type1:
    print(keys)

#Printing all values of keys
for values in type1:
    print(type1[values])


#Operations on Dictionaries
EXP1={"Name":"Vishal","Surname":"Mahajan","Age":18,"Roll No":63,"Branch":"IT A3"}

#1. Update() : Updates the dictionary with the specified key-value pairs
EXP1.update({"Age":20})
print("1. After Updating Age, Dicitonary is ",EXP1)

#2. copy() : Returns a copy of the dictionary
CopyEXP1=EXP1.copy()
print("2. Copy of EXP1 is ",CopyEXP1)

#3.Keys() : Returns a list containing the dictionary's keys
print("3.Keys in EXP1 is ",EXP1.keys())

#4.Values() : Returns a list of all the values in the dictionary
print("4.Values in EXP1 is ",EXP1.values())

#5. Items() : Returns a list containing a tuple for each key value pair
print("5. Items in EXP1 is ",EXP1.items())

#6. Get() : Returns the value of the specified key
print("6. Value of Name in EXP1 is ",EXP1.get("Name"))

#7. Pop() : Removes the element with the specified key
EXP1.pop("Age")
print("7. After Poping Age, EXP1 is ",EXP1)

#8. Popitem() : Removes the last inserted key-value pair
EXP1.popitem()
print("8. After Poping Last Inserted Key-Value Pair, EXP1 is ",EXP1)

#9. Setdefault() : Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
EXP1.setdefault("Age",18)
print("9. After Setting Default Age, EXP1 is ",EXP1)

#10. Clear() : Removes all the elements from the dictionary
EXP1.clear()
print("10. After Clearing EXP1, EXP1 is ",EXP1)


