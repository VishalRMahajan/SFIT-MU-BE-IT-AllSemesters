#Write a program to find the lowest number out of the three numbers entered by the user.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if(num1<num2 and num1<num3):
    print(num1,"is the lowest number")
elif(num2<num1 and num2<num3):
    print(num2,"is the lowest number")
else:
    print(num3,"is the lowest number")