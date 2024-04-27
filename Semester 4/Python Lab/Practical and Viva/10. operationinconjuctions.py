maths=int(input("Enter the marks of Maths: "))
#Using IF-ELIF-ELSE
if((maths>=65) and(maths<=75)):
    print("Student with",maths," marks have Grade B")
elif ((maths>=76) and (maths<=85)):
    print("Student with",maths," marks have Grade A")
elif (maths>86):
    print("Student with",maths," marks have Grade O")
else:
    print("Student with",maths," marks have Grade C")

#WAP to determine if the Character enteed is a vowel or not
print("\nWAP to determine if the Character enteed is a vowel or not")
char=input("Enter any character:")
if (char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
    print("Entered Char",char,"is vowel")
elif (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
    print("Entered Char",char,"is vowel")
else:
    print("Entered Char",char,"is consonant")