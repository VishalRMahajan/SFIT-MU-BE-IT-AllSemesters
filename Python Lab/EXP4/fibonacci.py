#Write a Python program to print Fibonacci series of 10 numbers using a while/for loop

#using for loop
print("Using For Loop")
a=0
b=1
for i in range(0,10):
    print(a , end=" ")
    c=a+b
    a=b
    b=c

#using while loop
print("\nUsing While Loop")
a=0
b=1
i=0
while i<10:
    print(a , end=" ")
    c=a+b
    a=b
    b=c
    i+=1