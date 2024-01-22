#List
#Declearing a List
EXP1= ["Vishal","Rajesh"]
print("Original List is",EXP1)

#1. Append() : Use to Add elements to the end of List
EXP1.append("Mahajan")
print("1. Appended List is",EXP1)

#2. Copy() :  Returns a copy of the list
CopyEXP1 = EXP1.copy()
print("2. Copyed List is  ",CopyEXP1)

#3. Extend() :Add the elements of a list (or any iterable)
#to the end of the current list

Extended_List=["SE","IT","A"]
EXP1.extend(Extended_List)
print("3. Extended List is",EXP1)

#4. Index() : Return lowest index where elements appears
index_of_mahajan=EXP1.index("Mahajan")
print("4. Index of Mahajan is ",index_of_mahajan)

#5. Remove() : Removes a given object from the List
EXP1.remove("SE")
print("5. After Removing SE List is",EXP1)

#6. Insert() : Adds an element at the specified position
EXP1.insert(3,"SE")
print("6. After Inserting SE List is",EXP1)

#7 Pop() : Removes the element at the specified position
EXP1.pop(5)
print("7. After Poping 5th element in List, List is",EXP1)

#8 Sort():Sorts the list
EXP1.sort()
print("8. After Sorting List, List is",EXP1)

#9. Reverse(): Reverses the order of the list
EXP1.reverse()
print("9. After reversing List, List is",EXP1)

#10 Count() : Returns the number of elements with specified value
count_of_SE=EXP1.count("SE")
print("10. Number of Times SE occured in List is",count_of_SE)

#11 Clear() ; Removes all the Elements from the List
EXP1.clear()
print("11. After reversing List, List is",EXP1)
