num = input("Enter the Number: ")
reverse = num[::-1]

print("Reverse of a number is",reverse)
if num == reverse:
    print("Entered Number is Palindrome")
else:
    print("Entered Number is not a Palindrome")