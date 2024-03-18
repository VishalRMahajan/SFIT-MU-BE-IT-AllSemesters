"""
Iterator: An iterator in Python is an object that can be iterated (looped) upon. An object which will return data, one element at a time.
Generator: A generator in Python is a function that returns an iterator. It looks like a normal function but contains yield statement.
yeild is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement.

"""

#Creating an iterator object using iter()
iterator = iter(["Vishal","Rajesh","Mahajan"])

#Iterator gives StopIteration error when it is exhausted so we use try and except block to handle it
print("\nIterator Ouptut using next() method of iterator object: ")
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

#Generator Function to generate a sequence of numbers
def my_generator(start, end):
    while start < end:
        yield start
        start += 1

#Printing the sequence of numbers using iterator object created by generator function
print("\nPrinting the sequence of numbers using iterator object created by generator function: ")
for i in my_generator(0, 5):
    print(i)