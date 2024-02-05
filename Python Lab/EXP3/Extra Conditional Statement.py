#WAP to convert lower to upper and upper to lower

print("\nWAP to convert lower to upper and upper to lower")
enteredString=input("Enter the String :")

if enteredString.isupper():
    print("Output String is",enteredString.lower())
else:
    print("Output String is",enteredString.upper())

#WAP to Display name of day in a week
print("\nWAP to Display name of day in a week")
day=int(input("Enter the Day:"))
if(day==1):
    print("Sunday")
elif(day==2):
    print("Monday")
elif(day==3):
    print("Tuesday")
elif(day==4):
    print("Wed")
elif(day==5):
    print("Thursday")
elif(day==6):
    print("Friday")
elif(day==7):
    print("Saturday")
else:
    print("There are only 7 days in a week")

#WAP to print month in Hindu Calender
print("\nWAP to print month in Hindu Calender")
month=int(input("Enter the Month:"))
if (month==1):
    print("Chaitra")
elif (month==2):
    print("Vaishak")
elif (month==3):
    print("Jaistha")
elif (month==4):
    print("Ashad")
elif (month==5):
    print("Shravan")
elif (month==6):
    print("Bhadrapad")
elif (month==7):
    print("Ashwin")
elif (month==8):
    print("kartik")
elif (month==9):
    print("Agrahayana")
elif (month==10):
    print("Paus")
elif (month==11):
    print("Maag")
elif (month==12):
    print("phalgun")
else:
    print("Invalid Month")

#WAP to Determine wheter a person is eligible to vote or not
print("\nWAP to Determine wheter a person is eligible to vote or not")
age=int(input("Enter the Person Age :"))
if age>=18:
    print("You are eligible to vote")
else:
    years=18-age
    print("You have to wait for",years,"to vote")

#WAP to increment a number if given number is positive
print("\nWAP to increment a number if given number is positive")
x=10
if (x>0):
    print("I am inside Loop",x)
    x=x+1
print("The Value of x is",x)
