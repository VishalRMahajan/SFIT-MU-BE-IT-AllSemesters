#List
list1=[1,2,3,4,5]
print("The List is", list1)
print("Index wise value i.e.0,1,2,3,4 as index")
print(list1[0],list1[1],list1[2],list1[3],list1[4])
print(type(list1))


#Tuple
tuple1=(1,2,3,4,5)
print("The tuple is ",tuple1)
print("Index wise value i.e.0,1,2,3,4 as index")
print(tuple1[0],tuple1[1],tuple1[2],tuple1[3],tuple1[4])

#Changing Element in Tuple using Index

list1[2]=1
print("The Updated List is", list1)

#tuple1[2]=1
#print("The Updated Tuple is", tuple1)

#List is Mutable and Tuples are Immutable

list2=["Hello","World"]
print("The Second List is", list2)

tuple2=["Hello","World"]
print("The Second Tuple is", tuple2)

list3=list1+list2
list4=list2+list1
print("List ",list1 ,"+ List ",list2, " is ", list3)
print("List ",list2 ,"+ List ",list3, " is ", list4)

#Sets

sets={"Python","Java","C++","Haskell","Prolog"}
print("The Sets is", sets)

sets.add("SQL")
print("Sets with added element is  ", sets)
sets.remove("SQL")
print("Sets with removed element is  ", sets)

