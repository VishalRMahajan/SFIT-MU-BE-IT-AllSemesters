
print("\nDivided by Zero Error Handling:")
def divide(num,dem):
    try:
        result = num/dem
    except ZeroDivisionError:
        print("Division by Zero is not Possible")
    else:
        print("Result is",result)
    finally:
        print("Execution Completed")

num = int(input("Enter the Numerator: "))
dem = int(input("Enter the Denominator: "))
divide(num,dem)

print("\nValue Error Handling:")
def ExceptionHandling():
    try:
        num = int(input("Enter the Number: "))
    except ValueError:
        print("Please Enter a Valid Number")
    else:
        print("Entered Number is",num)
    finally:
        print("Execution Completed")

ExceptionHandling()

print("\nIndex Error Handling:")
def IndexErrorHandling():
    try:
        arr = [1,2,3,4,5]
        index = int(input("Enter the Index: "))
        print("Element at the Given Index is",arr[index])
    except IndexError:
        print("Index Out of Range")
    else:
        print("Element Found")
    finally:
        print("Execution Completed")

IndexErrorHandling()

print("\nKey Error Handling:")
def KeyErrorHandling():
    try:
        dict = {"Name":"Vishal","Surname":"Mahajan"}
        key = input("Enter the Key: ")
        print("Value at the Given Key is",dict[key])
    except KeyError:
        print("Key Not Found")
    else:
        print("Key Found")
    finally:
        print("Execution Completed")

KeyErrorHandling()