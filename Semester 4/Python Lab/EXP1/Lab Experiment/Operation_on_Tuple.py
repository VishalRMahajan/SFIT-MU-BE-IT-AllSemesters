# Create a tuple
EXP1 = ("Vishal","Mahajan","IT","A3")

#Accessing Elements of Tuple
print("1. First Element of Tuple is ",EXP1[0])


#Built-in Functions on Tuple
#1. Count() : Returns the number of times a specified value occurs in a tuple
count_of_Vishal=EXP1.count("Vishal")
print("1. Number of Times Vishal occured in Tuple is",count_of_Vishal)

#2. Index() : Searches the tuple for a specified value and returns the position of where it was found
index_of_IT=EXP1.index("IT")
print("2. Index of IT is ",index_of_IT)

#3. len() : Returns the length of the tuple
length_of_tuple=len(EXP1)
print("3. Length of Tuple is ",length_of_tuple)

#4. max() : Returns the largest value in a tuple
max_of_tuple=max(EXP1)
print("4. Max of Tuple is ",max_of_tuple)

#5. min() : Returns the smallest value in a tuple
min_of_tuple=min(EXP1)
print("5. Min of Tuple is ",min_of_tuple)

#6. sum() : Sums the items of an iterator
EXP1_int=(1,2,3,4,5)
sum_of_tuple=sum(EXP1_int)
print("6. Sum of Tuple is ",sum_of_tuple)

#7. sorted() : Returns a sorted list of the specified iterable object
sorted_tuple=sorted(EXP1)
print("7. Sorted Tuple is ",sorted_tuple)

