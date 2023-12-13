"""
10 List Methods in Python are append(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort(),clear()
append()    Adds an element at the end of the list

copy()      Returns a copy of the list
count()     Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()     Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()       Removes the element at the specified position
remove()    Removes the item with the specified value
reverse()   Reverses the order of the list
sort()      Sorts the list
clear()     Removes all the elements from the list
"""

EXP1 =["Vishal","Kevin"]

append = EXP1.append("Ajay")
print(f"appended List is {EXP1}")

Copy= EXP1.copy()
print(f"Copyed List is {Copy}")

Extended_List = ["Subhodeep","Joseph"]
EXP1.extend(Extended_List)
print(f"Extended_List is {EXP1}")

indexofVishal=EXP1.index("Vishal")
print(f"Vishal is at {indexofVishal} position ")

poped=EXP1.pop(4)
print(f"Poped Element is {poped}")

EXP1.insert(1,"Shubham")
print(f"List after insertion is {EXP1}")

EXP1.remove("Kevin")
print(f"List after Removing Element is {EXP1}")

EXP1.reverse()
print(f"Reversed List is {EXP1}")

EXP1.sort()
print(f"Sorted List is {EXP1}")

EXP1.clear()
print(f"Cleared List is {EXP1}")