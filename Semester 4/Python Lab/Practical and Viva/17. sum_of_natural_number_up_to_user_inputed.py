#WAP to find the sum of natural numbers up to n,where n is provided  by the user.
print("WAP to find the sum of natural numbers up to n,where n is provided  by the user.")
num=int(input("Enter number upto which sum is to be Calculated: "))

print("\nUsing While Loop")
if num<0:
    print("Enter a Positive Integer")
else:
    temp=num
    sum=0
    while temp >0:
        sum=sum+temp
        temp=temp-1
    print("Sum of Number from 1 to",num,"is",sum)

print("\nUsing For Loop")
sum=0
if num<0:
    print("Enter a Positive Integer")
else:
    for i in range(1,num+1):
        sum=sum+i
    print("Sum of Number from 1 to",num,"is",sum)
