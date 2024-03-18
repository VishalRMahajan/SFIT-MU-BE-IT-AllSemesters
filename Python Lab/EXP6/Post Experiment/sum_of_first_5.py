#Write a Python program to calculate sum of first 5 natural numbers using recursion.

def sum_of_first_5(n):
    if n==1:
        return 1
    else:
        return n+sum_of_first_5(n-1)
    
print("\nSum of first 5 natural numbers is: ",sum_of_first_5(5))