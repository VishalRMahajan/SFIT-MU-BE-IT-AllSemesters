import math
import cmath
var1=int(input("Enter the First Number: "))
var2=int(input("Enter the Second Number: "))

print("\n1.Addition of ",var1,"and",var2,"is",var1+var2)
print("2.Subtraction of ",var1,"and",var2,"is",var1-var2)
print("3.Multiplication of ",var1,"and",var2,"is",var1*var2)
print("4.Division of ",var1,"and",var2,"is",var1/var2)
print("5.Floor Division of ",var1,"and",var2,"is",var1//var2)
print("6.",var1,"to the power",var2,"is",var1**var2)
print("7.Sqrt of",var1,"is",math.sqrt(var1),"and","Sqrt of",var2,"is",math.sqrt(var2))


comr1=int(input("Enter the real part of 1st complex number: "))
comi1=int(input("Enter the imaginary part of 1st complex number: "))
comr2=int(input("Enter the real part of 2nd complex number: "))
comi2=int(input("Enter the iamginary part of 2nd complex number: "))

com1=complex(comr1,comi1)
com2=complex(comr2,comi2)

