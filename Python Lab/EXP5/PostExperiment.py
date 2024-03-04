import array as arr

name = arr.array('u',["v","i","s","h","a","l"])
print(name)
length=len(name)
print(length)
middlename_len=int(input("Enter the len of middle name:"))

while (middlename_len !=0):
    char=input("Enter the name char by char: ")
    name.append(char)
    middlename_len=middlename_len-1

print(name)

name.extend(["m","a","h","a","j","a","n"])
print(name)

name.insert(6," ")
name.insert(13," ")
print(name)

print("First name is",name[:6])
print("Reverse is",name[::-1])
