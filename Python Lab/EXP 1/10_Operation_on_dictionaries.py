#Python Dictionaries

#Creating Dicitonaries
#Type 1
type1={"Name":"Vishal","Surname":"Mahajan","Age":"Eigtheen"}
print(type(type1))
print("The original Dicitonary is ",type1)

#Type2
type2= dict ({63:"Vishal",64:"Shubham"})
print("Dicitonary with use of dict() is ",type2)
print(type(type2))

#Type3
type3= dict([(63,"Vishal"),(64,"Shubham")])
print(type(type3))
print("Dicitonary with each item as a pair ",type3)

#Change the Values
type1["Age"]=20
print("The updated Dicitonary is ",type1)


#Printing all keys
for keys in type1:
    print(keys)

#Printing all values of keys

for values in type1:
    print(type1[values])
