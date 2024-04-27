def binarysearch(arr,element):
    start = 0
    end = len(arr) - 1

    for _ in range(len(arr)):
        mid = start + (end - start) // 2

        if arr[mid] == element:
            print("Element Found in the Given array")
            break
        elif arr[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print("Element Not Found") 


num = int(input("Enter the Number of Elements: "))
arr = []
for i in range(num):
    arr.append(int(input("Enter the Element: ")))

element = int(input("Enter the Element to be Searched: "))

arr.sort()
binarysearch(arr,element)
      

