PracticalSet1 = {"Vishal", "Mahajan", "SE-IT-A3"}
PracticalSet2 = {"Roll no 63","SE-IT-A3"}

#1. add : Add an element to the set
PracticalSet1.add("Roll no 63")
print("After Adding, Set is",PracticalSet1)

#2. remove : Remove the specified element
PracticalSet1.remove("Roll no 63")
print("After Removing, Set is",PracticalSet1)

#3. Union : Return a set containing the union of sets
Union = PracticalSet1.union(PracticalSet2)
print("After Union",Union)

#4. intersection : Return a set, that is the intersection of two other sets
Intersection = PracticalSet1.intersection(PracticalSet2)
print("After Intersection",Intersection)

#5. copy : Return a copy of the set
CopiedSet = PracticalSet1.copy()
print("Copied Set is", CopiedSet)

#6. difference : Return a set containing the difference between two or more sets
Difference = PracticalSet1.difference(PracticalSet2)
print("After Difference",Difference)

#7. issubset : Returns whether another set contains this set or not
subset = {'Vishal','Mahajan'}
print("Is subset?", subset.issubset(PracticalSet1))

#8. superset : Returns whether this set contains another set or not
print("Is superset?",PracticalSet1.issuperset(subset))

#9. pop : Remove an element from the set
PracticalSet1.pop()
print("After poping",PracticalSet1)

#10.clear : Remove all elements from the set
PracticalSet1.clear()
print(PracticalSet1)