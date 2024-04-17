#Maths Functions

#Importing Libraries
import math
import cmath

#General Terms
#math.pi (Calling π(radian) through dot using math lib.)

#1. Getting Values in Degrees and Radians
#radians = degress * π(here 3.14159) /180 deg
#Degrees()- Convert Radians to Degrees
print("\nConverting Radians into degress using math.degrees()")
print("pi/2 in degrees is ",math.degrees((math.pi/2)))
print("pi/4 in degrees is ",math.degrees((math.pi/4)))
print("pi in degrees is ",math.degrees((math.pi)))
print("pi/37 in degrees is ",math.degrees((math.pi/37)))

#Radians()- Convert Degree to Radians
print("\nConverting Degrees into radians using math.radians()")
print("90 in radians is",math.radians(90))
print("45 in radians is",math.radians(45))
print("180 in radians is",math.radians(180))
print("4.86 in radians is",math.radians(4.86))

#2. Getting values of Sin,cos and tan in radians
print("\nGetting values of Sin, Cos and tan in radians using math.sin(), math.cos() and math.tan()")
print("Sin(pi/2) is ", math.sin(math.pi/2))
print("Cos(pi/2) is ", math.cos(math.pi/2))
print("tan(pi)   is ", math.tan(math.pi))



#3. Getting arc Values
print("\nGetting arc Values (Output is in Radians) using math.asin(), math.acos() and math.atan()")
print("Sin inverse of 1 is ",math.asin(1))
print("Cos inverse of 0 is",math.acos(0))
print("Tan inverse of 1 is",math.atan(1))


#Complex Declearation
x=1.0
y=1.0
z= complex(x,y)
print("\nComplex Number using ",x, " and ",y," is ",z)


#4. Getting Inverse of Complex Number
print("\nGetting Inverse of Complex Number using cmath.asin(), cmath.acos() and cmath.atan()")
print("The arc sine of ",z," is ",cmath.asin(z))
print("The arc cosine of ",z," is ",cmath.acos(z))
print("The arc tangent of ",z," is ",cmath.atan(z))

#5. Finding the Exponantial of the sepcified value
print("\nFinding the Exponantial of the sepcified value using math.exp()")
print("e raised to 1 is ",math.exp(1))
print("e raised to 65 is ",math.exp(65))
print("e raised to -6.89 is ",math.exp(-6.89))

#6.Finding absolute value in float
print("\nFinding absolute value in float using math.fabs() and abs()")
print("Absolute value of -63 is (using fabs) ",math.fabs(-63))
print("Absolute value of -63 is (using abs) ",abs(-63))

#7. Finding Factorial of a Number
print("\nFinding Factorial of a Number using math.factorial()")
print("Factorial of 5 is ",math.factorial(5))
print("Factorial of 6 is ",math.factorial(6))
print("Factorial of 10 is ",math.factorial(10))

#8.Rounding Number down to the nearest integer
print("\nRounding down to nearest integer using Floor() function")
print("Round of -1.5 is ",math.floor(-1.5))
print("Round of -1.4 is ",math.floor(-1.4))
print("Round of -1.3 is ",math.floor(-1.3))
print("Round of -1.2 is ",math.floor(-1.2))
print("Round of -1.1 is ",math.floor(-1.1))
print("Round of 0 is ",math.floor(0))
print("Round of 0.1 is ",math.floor(0.1))
print("Round of 0.2 is ",math.floor(0.2))
print("Round of 0.3 is ",math.floor(0.3))
print("Round of 0.5 is ",math.floor(0.5))
print("Round of 0.9 is ",math.floor(0.9))

#9.Returning th reminder of x/y
print("\nReturning Remainder using fmod() function")
print("remainder of 20/4 is",math.fmod(20,4))
print("remainder of 20/3 is",math.fmod(20,3))
print("remainder of 15/6 is",math.fmod(15,6))
print("remainder of -10/3 is",math.fmod(-10,3))

#10.Returning mantissa and exponent of number
print("\nReturning mantissa and exponent of number using frexp() function")
print("(Mantissa and Exponent) of 4 is",math.frexp(4))
print("(Mantissa and Exponent) of -4 is",math.frexp(-4))
print("(Mantissa and Exponent) of 7 is",math.frexp(7))

#11.Print the Sum of all items
print("\nPrint the Sum of items using fsum() function")
print("Sum of [1,2,3,4,5] is ",math.fsum([1,2,3,4,5]))
print("Sum of [100,400,340,500] is ",math.fsum([100,400,340,500]))
print("Sum of (1.7,0.3,1.5,4.5) is ",math.fsum((1.7,0.3,1.5,4.5)))

#12.Finding Gcd of the two integer
print("\nFinding the Gcd of Integer using gcd() function")
print("Gcd of 3 and 6 is ",math.gcd(3,6))
print("Gcd of 6 and 12 is ",math.gcd(6,12))
print("Gcd of 36 and 12 is ",math.gcd(36,12))

#13.Compare the closeness of two values
print("\nComparing Closeness using isclose() function")
print("Is 1.21 close to 1.21 :",math.isclose(1.21,1.21))
print("Is 1.223 close to 1.4566 :",math.isclose(1.223,1.4566))
print("Is 1.233 close to 1.233000001 :",math.isclose(1.233,1.233000001))
print("Is 1.227 close to 1.230 :",math.isclose(1.227,1.230))

#14. Comparing Closeness upto provided values 
print("\nComparing Closeness using isclose() and abs_tol function")
print("Is 8.005 close to 8.450 upto 0.4 :", math.isclose(8.005,8.450,abs_tol =0.4))
print("Is 8.005 close to 8.450 upto 0.5 :", math.isclose(8.005,8.450,abs_tol =0.5))


#15.Raised to Function
print("\nGetting x to the power y using pow() function")
print("9 to the power 3 is", math.pow(9,3))


#16.Returning the Natural logarithm of Different Number
print("\nReturning the Natural logarithm of Different Number using log() function")
print("Natural log of 2.7183 is ",math.log(2.7183))
print("Natural log of 2 is ",math.log(2))
print("Natural log of 1 is ",math.log(1))

#17.Returning the base-10 logarithm of Different Number
print("\nReturning the base-10 logarithm of Different Number using log10() function")
print("base-10 log of 2.7183 is ",math.log10(2.7183))
print("base-10 log of 2 is ",math.log10(2))
print("base-10 log of 1 is ",math.log10(1))

print("\nSome Basic parameter using math lib:")
#Print the Value of e
print("Value of e is ",math.e)

#Print the Positive Infintiy
print("Value of Positive Infinity is  ",math.inf)

#Print the Negative Infintiy
print("Value of Negative Infinity is ",-math.inf)



