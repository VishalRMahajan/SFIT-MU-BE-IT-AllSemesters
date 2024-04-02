"""Write a Python program to understand slicing and indexing of arrays"""
import array

# Create an array
arr = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])

# Indexing: Accessing an element of the array using its index
print("Element at index 3:", arr[3])

# Slicing: Getting a subset of the array using a range of indices
print("Elements from index 2 to 5:", arr[2:6])

# Negative indexing: Accessing elements from the end of the array
print("Last element of the array:", arr[-1])

# Negative slicing: Getting a subset from the end of the array
print("Elements from the third last to the end of the array:", arr[-3:])