import array as arr
#original array
numbers=arr.array("i",[10,20,30])
print("Original array is",numbers)
print("\nChanging the First element to 40")
numbers[0] = 40
print("Updated Array is",numbers)

numbers.append(50)
print("Adding element 50 using append method is",numbers)

numbers.insert(0,5)
print("Inserting element using insert method is",numbers)

numbers.extend([60,70,80])
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop(0)
print(numbers)


