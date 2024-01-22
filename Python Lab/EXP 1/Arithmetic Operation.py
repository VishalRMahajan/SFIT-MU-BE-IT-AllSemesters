#Arithmetic Operation (Binary Operators)

print(2+2)  #Addition
print(10-5) #Subtraction
print(5*2)  #Mulitplcation
print(8/5)  #Division (Gives Float)
print(8//5) #Division but trucate the decimal (Gives Int)
print(17%3) #Give Remainder
print(2**3) #2 rasied to 3


#Operator Precedance
#[Mulitplication, Modulo, addition and Subtraction]
# Mulitplication,Division and Modulo has the same precedance.
#Operators with same presedance are evaluated from left to right
print("The Ouput is ")
print(5+2*4%6-1)
print(5%3*5)
print(5/3%2*3)

#Unary Operators
a=-5
b=+5
c=a+b
print(a)
print(b)
print(c)


#Code for Addition
print("Addition")
var1=input('Enter the First Number: ')
var2=input('Enter the Second Number: ')
var1=int(var1)
var2=int(var2)
add=var1+var2
print("The Addition is ",add )
print(type(add))

#Code for Subtraction
print("Subtraction")
var1=input('Enter the First Number: ')
var2=input('Enter the Second Number: ')
var1=int(var1)
var2=int(var2)
subtract=var1-var2
print("The Difference is ",subtract )
print(type(subtract))

"""
Program for Arithmetic Operators with user input and
type Casting it to int as input will be str by default

"""
Xa = float(input("Enter the First Number: "))
Xb = float(input("Enter the Second Number: "))
add = Xa +Xb
diff = Xa-Xb
mul = Xa * Xb
div= Xa /Xb
floor_div = Xa//Xb
power = Xa ** Xb
modulus = Xa % Xb
print(" Sum of the Numbers ",Xa, 'and',Xb,'is ',add)
print(" Diff of the Numbers ",Xa, 'and',Xb,'is ',diff)
print(" Product of the Numbers ",Xa, 'and',Xb,'is ',mul)
print(" Division of the Numbers ",Xa, 'and',Xb,'is ',div)
print(" Floor Division of the Numbers ",Xa, 'and',Xb,'is ',floor_div)
print(" Power of the Numbers ",Xa, 'and',Xb,'is ',power)
print(" Modulus of the Numbers ",Xa, 'and',Xb,'is ',modulus)

         
