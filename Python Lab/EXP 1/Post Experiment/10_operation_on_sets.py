# Create a set with the given names
PostEXP = {'Vishal', 'Rajesh', 'Mahajan', 'SE', 'IT', 'A'}
print("\nSet POSTEXP is: ", PostEXP)
PostEXP2 = {'Python', 'Lab','SE', 'IT', 'A'}
print("Set POSTEXP2 is: ", PostEXP2)

# 1. set.add(): Adds an element to the set
PostEXP.add('Roll no 63')
print("\n1.After adding an element to the set, set is: ", PostEXP)

# 2. set.remove(): Removes an element from the set
PostEXP.remove('A')
print("2.After removing an element from the set, set is: ", PostEXP)

# 3. Element in set: Check if an element is present in the set
print("3.Check if an element Vishal is present in the set POSTEXP: ", 'Vishal' in PostEXP)

# 4. len(set): Get the length of the set
print("4.Length of the set POSTEXP is: ", len(PostEXP))

# 5. set.copy(): Copy the set
PostEXP_copy = PostEXP.copy()
print("5.Copy of the set POSTEXP is: ", PostEXP_copy)

# 6. set.difference(): Get the difference between two sets
difference = PostEXP.difference(PostEXP2)
print("6.Difference between two sets POSTEXP and PostEXP2 is: ", difference)

# 7. set.intersection(): Get the intersection between two sets
intersection = PostEXP.intersection(PostEXP2)
print("7.Intersection of two sets POSTEXP and PostEXP2 is: ", intersection)

# 8. set.issubset(): Check if a set subset is a subset of another set
subset = {'Vishal', 'Rajesh'}
print("8.Check if a set subset is a subset of another set POSTEXP: ", subset.issubset(PostEXP))

# 9. set.union(): Get the union between two sets
union = PostEXP.union(PostEXP2)
print("9.Union of two sets POSTEXP and PostEXP2 is: ", union)

# 10. set.clear(): Clear all elements from the set
PostEXP.clear()
print("10.After clearing all elements from the set, set is: ", PostEXP)