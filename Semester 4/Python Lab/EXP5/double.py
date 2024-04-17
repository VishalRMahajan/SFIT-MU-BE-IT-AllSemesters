"""Write a Python program to create an array of double data type. Using this array, create another array whose elements are three times that of the elements of the first array.
"""

# Using the array module
import array

arr = array.array('d', [1.1, 2.2, 3.3, 4.4])
print(arr)

# Using list comprehension
arr2 = array.array('d', [i*3 for i in arr])
print("\nElements of the new array are three times that of the original array:")
print(arr2)