#WAP to define function to evaluate if the number is odd or even
print("\nWAP to define function to evaluate if the number is odd or even")
def evenodd(x):
    if (x%2==0):
        print(x,"is Even")
    else:
        print(x,"is Odd")

x = int(input("Enter the Number to be checked :"))
evenodd(x)

#WAP to add two numbers
print("\nWAP to add two numbers using function")
def addtwo(num1,num2):
    sum=num1+num2
    print("Sum of",num1,"and",num2,"is",sum)

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
addtwo(num1,num2)

#WAP to find square of a number using fun.Use return statement
print("\nWAP to find square of a number using fun.Use return statement")
def sqr(num):
    ans=num*num
    return ans
num = int(input("Enter the number :"))
square = sqr(num)
print("Square is ",square)

#WAP to find factorial using recursive function
print("\nWAP to find factorial using recursive function")
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num = int(input("Enter the number of which factorial to be cal :"))
print("Factorial of",num,"is",fact(num))
