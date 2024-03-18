def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x :
            return i
    return -1

x = int(input("Enter the Number to be searched :"))
arr =[10,20,60,33,46,78,94,63]

if search(arr,x)== -1 :
    print("No such element found")
else:
    print(x,"is found at",search(arr,x))
