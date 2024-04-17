a=int(input("Enter the First Number on which  Operation is to be Performed : "))
b=int(input("Enter the Second Number on which Operation is to be Performed : "))

#1. Arithmetic Operators
print("\nArithmetic Operators")
print("Addition of ",a," and ",b," is ",a+b)
print("Subtraction of ",a," and ",b," is ",a-b)
print("Multiplication of ",a," and ",b," is ",a*b)
print("Division of ",a," and ",b," is ",a/b)
print("Modulus of ",a," and ",b," is ",a%b)
print("Exponent of ",a," and ",b," is ",a**b)
print("Floor Division of ",a," and ",b," is ",a//b)

#2. Comparison Operators
print("\nComparison Operators")
print("Is ",a," greater than ",b," : ",a>b)
print("Is ",a," less than ",b," : ",a<b)
print("Is ",a," equal to ",b," : ",a==b)
print("Is ",a," not equal to ",b," : ",a!=b)
print("Is ",a," greater than or equal to ",b," : ",a>=b)
print("Is ",a," less than or equal to ",b," : ",a<=b)

#3. Bitwise Operators
print("\nBitwise Operators")
print("Bitwise AND of ",a," and ",b," is ",a&b)
print("Bitwise OR of ",a," and ",b," is ",a|b)
print("Bitwise XOR of ",a," and ",b," is ",a^b)
print("Bitwise NOT of ",a," is ",~a)
print("Bitwise Left Shift of ",a," by 2 is ",a<<2)
print("Bitwise Right Shift of ",a," by 2 is ",a>>2)

#4. Assignment Operators
print("\nAssignment Operators")
c=b
print("The Value of c is ",c)
c+=b
print("The Value of c+=b is ",c)
c-=b
print("The Value of c-=b is ",c)
c*=b
print("The Value of c*=b is ",c)
c/=b
print("The Value of c/=b is ",c)
c%=b
print("The Value of c%=b is ",c)
c**=b
print("The Value of c**=b is ",c)
c//=b
print("The Value of c//=b is ",c)


#5. Logical Operators
print("\nLogical Operators")
print("True and True is ",True and True)
print("True or False is ",True or False)
print("not True is ",not True)
