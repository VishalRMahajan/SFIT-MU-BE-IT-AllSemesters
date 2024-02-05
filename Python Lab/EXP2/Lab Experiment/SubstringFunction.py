#Python Code for substring Operation

ini_string= "abcdefghijklmnop"
print("Inital String is",ini_string)

print("\nSubstring using [:num]")
start5char=ini_string[:5]
last5char=ini_string[5:]
print("Five char [:5] from start is",start5char)
print("Rest of String After 5 char [5:] is",last5char)

charwithgap1= ini_string[::2]
charwithgap2= ini_string[::3]
print("String with gap 1 [::2] is ",charwithgap1)
print("String with gap 2 [::3] is ",charwithgap2)
