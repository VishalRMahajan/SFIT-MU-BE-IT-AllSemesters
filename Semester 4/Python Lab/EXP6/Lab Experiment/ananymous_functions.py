#WAP To implement anonymous functions(lambda,map,reduce,filter) 

# Using Lambda
#Lambda is a small anonymous function. It can take any number of arguments, but can only have one expression.
print("\nUsing Lambda")
f=lambda x:x*x
print(f(5))

# Using Map
#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
print("\nUsing Map")
def square(x):
    return x*x
numbers=[1,2,3,4,5]
result=map(square,numbers)
print(list(result))

# Using Reduce
#The reduce() function is defined in the functools module. It applies a rolling computation to sequential pairs of values in a list.
print("\nUsing Reduce")
from functools import reduce
def add(x,y):
    return x+y
numbers=[1,2,3,4,5]
result=reduce(add,numbers)
print(result)


# Using Filter
#The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
print("\nUsing Filter")
def is_even(x):
    return x%2==0
numbers=[1,2,3,4,5,6,7,8,9,10]
result=filter(is_even,numbers)
print(list(result))
