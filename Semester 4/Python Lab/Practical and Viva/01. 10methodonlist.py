#Creating a List
Practical = ["Vishal","Mahajan"]

#1. Append : Add element to the end of the list 
Practical.append("SE-IT-A3")
print("After Appending, List is",Practical)

#2. Insert : Add element at the specified index
Practical.insert(1,"Rajesh")
print("After Inserting, List is",Practical)

#3. Index : Return the index of the first element with the specified value
indexofVishal= Practical.index("Vishal")
print("Vishal is at",indexofVishal,"index")

#4. Remove : Remove the first item with the specified value
Practical.remove("SE-IT-A3")
print("After Removing SE-IT-A3, List is",Practical)

#5. Copy : Returns a copy of the list
CopiedPractical = Practical.copy()
print("Copied List is",CopiedPractical)

#6. Extend : Add the elements of a list (or any iterable), to the end of the current list
ExtendList= ["SE","IT-A","63"]
Practical.extend(ExtendList)
print("After Extending, List is",Practical)

#7. Pop : Removes the element at the specified position
Practical.pop()
print("After Popping, List is",Practical)

#8. Reverse : Reverses the order of the list
Practical.reverse()
print("After Reversing, List is",Practical)

#9. Sort : Sorts the list
Practical.sort()
print("After Sorting, List is",Practical)

#10. Count : Returns the number of elements with the specified value
CountOfVishal =Practical.count("Vishal")
print("Vishal occured",CountOfVishal,"times in the list")

#11. Clear : Removes all the elements from the list
Practical.clear()
print("After Clearing, List is",Practical)