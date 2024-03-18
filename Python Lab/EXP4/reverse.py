#Write a program to print a number in reverse order. 

#using for loop
print("Using For Loop")
num=int(input("Enter the number to print in reverse order: "))
rev=0
temp=num
for i in range(0,len(str(temp))):
    rev=rev*10+temp%10
    temp=temp//10
print("Reverse of the number is",rev)

#using while loop
rev=0
print("\nUsing While Loop")
while num>0:
    rev=rev*10+num%10
    num=num//10
print("Reverse of the number is",rev)