"""To implement a Python program to demonstrate use of Python arrays """

import array

#creating an array
arr=array.array("i",[1,2,3,4,5])

#printing the original array
print("\nThe original array is",arr)

#changing the first element to 10
arr[0]=10
print("\nChanging the first element to 10 is",arr)

#adding element 63 using append method
arr.append(63)
print("\nAdding element 63 using append method is",arr)

#inserting element 0 at the beginning of the array
arr.insert(0,0)
print("\nInserting element 0 at the beginning of the array is",arr)

#extending the array with elements 6,7,8
arr.extend([6,7,8])
print("\nExtending the array with elements 6,7,8 is",arr)

#removing element 0 from the array
arr.remove(0)
print("\nRemoving element 0 from the array is",arr)

#removing the first element from the array
arr.pop(0)
print("\nRemoving the first element from the array is",arr)