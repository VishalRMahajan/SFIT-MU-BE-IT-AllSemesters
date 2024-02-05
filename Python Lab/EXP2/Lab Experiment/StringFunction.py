"""
String Lower and Upper Operation
1. string.lower() converts the string to lower case
2. string.upper() converts the string to upper case
3. string.islower() returns True if all the characters in the string are in lower case
4. string.isupper() returns True if all the characters in the string are in upper case
"""
print("\nString Lower and Upper Operation using string.lower() and string.upper()")
string1="HELLO WORLD"
print("Original String is",string1)
print("\n1. Lowered String using string.lower() is",string1.lower())
print("2. Is the string",string1," in Uppercase :",string1.isupper())
print("3. Is the string",string1," in Lowercase :",string1.islower())

string2="Hello World"
print("\n4. Uppered String using string.upper() is",string2.upper())
print("Is the string",string2," in Uppercase :",string2.isupper())

"""
String Concatenation Using + operator, join() method and format() function
5. join() method is use to combine the strings
6. format() function is use to concatenate the strings
"""
print("\nString Concatenation")
First="Vishal"
Surname=" Mahajan"
Class=" SE IT A3"
Fullname= First+Surname
Entire= First+Surname+Class
print("The Concatenated String is ",Fullname)
print("The next Concatendated String is "+ Fullname +" Student")
print("Completed Three Variable Concat is "+Entire)

#String Concatenantion using join() method
print("\n5. The Concatented String Using .join() is "+"".join([First,Surname,Class]))
#String Concatenantion using format() function
print("\n6. Output Using Format")
txt1="My name is {name}, I'm {age} year old".format(name="Vishal Rajesh Mahajan",age=20)
print(txt1)
txt2="My name is {0}, I'm {1} year old".format("Vishal Rajesh Mahajan",20)
print(txt2)
txt3="My name is {}, I'm {} year old".format("Vishal Rajesh Mahajan",20)
print(txt3)

txt="I am {:<8} year old."
print("\nUsing :< for left align : ",txt.format(20))
txt="I am {:>8} year old."
print("Using :> for right align : ",txt.format(20))
txt="I am {:^8} year old."
print("Using :^ for center-align align : ",txt.format(20))

a="Python"
print("\nUsing * to multiply the String by 3 times : ",a*3)

"""
String Split and Replace Operation
7. string.split() method is use to split the string
8. string.replace() method is use to replace the string
"""
print("\nString Split and Replace Operation")
string3="Vishal Rajesh Mahajan"
print("Original String is ",string3)
print("7. Splitting the String using string.split() is ",string3.split())
print("   Splitting the String using string.split('a') is ",string3.split('a'))
print("8. Replacing the String using string.replace('l','b') is ",string3.replace('l','b'))


"""
9. string.find() method is use to find the string
10. string.index() method is use to find the string
11. string.count() method is use to count the string
"""
print("\nString Find, Index, Count Operation")
string4="Vishal Rajesh Mahajan"
print("Original String is ",string4)
print("9. Finding the char using string.find('l') is ",string4.find('l'))
print("10. Finding the char using string.index('l') is ",string4.index('l'))
print("11. Counting the number of char in string using string.count('a') is ",string4.count('a'))
print("\n")

