print("\nWAP to test whether a number entered by the user is negative,positiveor equal to zero")
num=int(input("Enter any number between Positive or Negative: "))
if(num>0):
    print("Entered Number",num,"is Posititve")
elif(num<0):
    print("Entered Number",num,"is Negative")
else:
    print("Entered Number",num,"is Zero")