num = int(input("Enter the Number of Elements: "))
arr = []
for i in range(num):
    arr.append(int(input("Enter the Element: ")))

element = int(input("Enter the Element to be Searched: "))

for i in range(len(arr)):
    if arr[i] == element:
        print("Element found at",i,"index")
        break
else:
    print("Element Not Found")