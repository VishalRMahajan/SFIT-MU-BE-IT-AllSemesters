
print("Division by zero exception:")
def zero_exception(num1,num2):
    try:
        divide=num1/num2
    except ZeroDivisionError as e :
        print(e)
         
zero_exception(10,0)


print("\nIndex out of range exception:")
def array_exception():
    try:
        arr=[1,2,3,4,5]
        print(arr[5])
    except IndexError as e:
        print(e)
array_exception()