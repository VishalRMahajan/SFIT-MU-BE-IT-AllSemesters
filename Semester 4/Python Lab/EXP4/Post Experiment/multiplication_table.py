#WAP to print tables
print("\nWAP to Print  tables using Loops")
table=int(input("Enter the Number to print the table: "))
print("Using For Loop")
n=1
for i in range(0,10):
    print(table,"*",i+1,"is",table*(i+1))

print("\nUsing While Loop")
while (n<=10):
    print(table,"*",n,"is",table*(n))
    n=n+1