"""Write a Python program to understand various methods of array class.
"""

import array

# Create an array
arr = array.array('i', [10, 20, 30, 40, 50])

print("Original array:", arr)

# append(): Adds an element to the end of the array
arr.append(60)
print("After appending 60:", arr)

# extend(): Adds multiple elements to the end of the array
arr.extend([70, 80, 90])
print("After extending with [70, 80, 90]:", arr)

# insert(): Inserts an element at a specific position
arr.insert(0, 0)
print("After inserting 0 at position 0:", arr)

# remove(): Removes the first occurrence of an element
arr.remove(50)
print("After removing 50:", arr)

# pop(): Removes and returns the element at a specific position
print("Popped element:", arr.pop(3))
print("After popping element at position 3:", arr)

# reverse(): Reverses the array
arr.reverse()
print("After reversing:", arr)

# count(): Returns the number of occurrences of an element
print("Count of 10:", arr.count(10))

# tolist(): Converts the array to a list
print("Array converted to list:", arr.tolist())

