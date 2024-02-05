#If-elif-else statement

#WAP to test Entered Number is Even or Odd
print("\nWAP to test Entered Number is Even or Odd")
num=int(input("Enter the Number to be Checked: "))
if (num %2 ==0):
    print("Entered Number",num,"is even")
else:
    print("Entered Number",num,"is odd")

#WAP to grade the Student based on marks
print("\nWAP to grade the Student based on marks")
maths=int(input("Enter the marks of Maths: "))

#Using Only IF
if((maths>=65) and(maths<=75)):
    print("Grade B")
if ((maths>=76) and (maths<=85)):
    print("Grade A")
if (maths>86):
    print("Grade O")
if maths<=64:
    print("Grade C")



#Using IF-ELIF-ELSE
if((maths>=65) and(maths<=75)):
    print("Grade B")
elif ((maths>=76) and (maths<=85)):
    print("Grade A")
elif (maths>86):
    print("Grade O")
else:
    print("Grade C")

#WAP to determine if the Character enteed is a vowel or not
print("\nWAP to determine if the Character enteed is a vowel or not")
char=input("Enter any character:")
if (char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
    print("Entered Char",char,"is vowel")
elif (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
    print("Entered Char",char,"is vowel")
else:
    print("Entered Char",char,"is consonant")



#WAP to test whether a number entered by the user is negative,positive
#or equal to zero
print("\nWAP to test whether a number entered by the user is negative,positiveor equal to zero")
num=int(input("Enter any number between Positive or Negative: "))
if(num>0):
    print("Entered Number",num,"is Posititve")
elif(num<0):
    print("Entered Number",num,"is Negative")
else:
    print("Entered Number",num,"is Zero")

    


