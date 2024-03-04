#While Loop in Python

#WAP To print 4 times
count=0
while (count<4):
    count=count+1
    print(count,"Vishal Mahajan")


#WAP to print Condition based on True or False
print("\nWAP to print Condition count < 3 based on True or False")
count=0
while (count<3):
    count=count+1
    print(count,"Condition is True")
else:
    print(count,"Condition is False")


#WAP to print Current Loop Status Using For Loop
print("\nWAP to print Current Loop Status Using For Loop (n=4)")
n=4
for i in range(0, n):
    print(i,"I am in For Loop")
print(n,"I am Outside the For Loop")

#WAP to print each element in the list
print("\nWAP to print each element in the list")
list1= ["Vishal","Rajesh","Mahajan","SE IT A","Roll no 63"]
for index in range(len(list1)):
    print("Element at",index,"is",list1[index])

#WAP to print tables
print("\nWAP to Print 2 tables using Loops")
print("Using For Loop")
n=1
for i in range(0,10):
    print("2 *",i+1,"is",2*(i+1))

print("\nUsing While Loop")
while (n<=10):
    print("2 *",n,"is",2*(n))
    n=n+1

print("\nWAP to Print table using Loops and User Input")
table=int(input("Enter the Number to print the table: "))
for i in range(0,10):
    print(table,"*",i+1,"is",table*(i+1))

print("\nNested Loop")
for i in range(1,5):
    for j in range(1,5):
        print("Hello",i,j)

    



