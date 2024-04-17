"""
Write a Python program to read marks of 3 subjects of a student and check 
if the average marks are above 50 then print that student is passed in exam
"""

Sub1=int(input("Enter the marks of Subject 1: "))
Sub2=int(input("Enter the marks of Subject 2: "))
Sub3=int(input("Enter the marks of Subject 3: "))

avg=(Sub1+Sub2+Sub3)/3

if(avg>50):
    print("Student is Passed with average ",avg)
else:
    print("Student is Failed with average ",avg)
