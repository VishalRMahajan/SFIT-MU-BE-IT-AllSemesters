#WAP to find the sum of natural numbers up to n,where n is provided  by the user.
print("\nWAP to find the sum of natural numbers up to n,where n is provided  by the user.")
num=int(input("Enter number upto which sum is to be Calculated:"))
if num<0:
    print("Enter a Positive Integer")
else:
    temp=num
    sum=0
    while num >0:
        sum=sum+num
        num=num-1
    print("Sum of Number from 1 to",temp,"is",sum)
