import array

arr = array.array('i', [1, 2, 3, 4, 5])
print("Original Array is",arr)

threetimearr = array.array('i',[3*i for i in arr])
print("Three Time Array is",threetimearr)

print("First three element of",arr,"is",arr[0:3])
print("First element in the ",arr,"is",arr[0])

arr.append(63)
print("After Adding element 63 , array becomes",arr)

print("Index of element 63 in",arr,"is",arr.index(63))

arr.remove(63)
print("After Removing element 63 , array becomes",arr)

print("Count of element 63 in array is",arr.count(63))

arr.extend([7,8,9])
print("Extended Array is",arr)

print("Poping the element from array",arr.pop())

arr.reverse()
print("Reversed array is",arr)