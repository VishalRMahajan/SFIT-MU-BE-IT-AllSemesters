"""
Write a python program to read marks of 3 subjects of 10 students and print total marks and average of each student. Also print the message if average is greater than 50 they are “pass”
"""

print("\nUsing For Loop")
for i in range(0,10):
    print("Student",i+1)
    total=0

    for j in range(0,3):
        marks=int(input("Enter the marks of Subject "+str(j+1)+": "))
        total=total+marks
    average=total/3

    print("Total Marks of Student",i+1,"is",total)
    print("Average Marks of Student",i+1,"is",average)
    if average>50:
        print("Student is Pass")
    else:
        print("Student is Fail")

print("\nUsing While Loop")
i=0
while i<10:
    print("Student",i+1)
    total=0
    j=0
    while j<3:
        marks=int(input("Enter the marks of Subject "+str(j+1)+": "))
        total=total+marks
        j+=1
    average=total/3

    print("Total Marks of Student",i+1,"is",total)
    print("Average Marks of Student",i+1,"is",average)
    if average>50:
        print("Student is Pass")
    else:
        print("Student is Fail")
    i+=1