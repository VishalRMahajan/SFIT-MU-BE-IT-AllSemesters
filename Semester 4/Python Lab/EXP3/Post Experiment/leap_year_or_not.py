#Write a program to check whether the input year is a leap year or not.

year=int(input("Enter the year to be checked: "))

if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(year,"is a Leap Year")
        else:
            print(year,"is not a Leap Year")
    else:
        print(year,"is a Leap Year")