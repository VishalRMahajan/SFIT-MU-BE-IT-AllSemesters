#Write a program to calculate factorial of a given number using a for loop.

#using for loop
print("Using For Loop")
num=int(input("Enter the number to calculate the factorial: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of",num,"is",fact)

#using while loop
print("Using While Loop")
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print("Factorial of",num,"is",fact)
