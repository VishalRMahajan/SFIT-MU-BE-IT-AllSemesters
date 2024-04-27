print("\nSquaring using Lambda Function")
lam = lambda x:x**2
num = int(input("Enter the Number to be Squared: "))
print("Square using lambda Function is",lam(num))

print("\nSquaring a entire List using Map function")
def squarefunction(num):
    return num**2
squarelist = [1,2,3,4,5,6,7,8,9,10]
result=map(squarefunction,squarelist)
print("Squared List of",squarelist,"is",list(result))

print("\nCalculating Addition using Reduce")
from functools import reduce
def add(x,y):
    return x+y
reducelist = [1,2,3,4,5,6,7,8,9,10]
print("Sum of elements in list",reducelist,"is",reduce(add,reducelist))

print("\nFiltering Even number in the List using Filter")
def iseven(num):
    return num %2 == 0

filterlist =[1,2,3,4,5,6,7,8,9,10]
print("Filtered Even Number from the list",filterlist,"is",list(filter(iseven,filterlist)))