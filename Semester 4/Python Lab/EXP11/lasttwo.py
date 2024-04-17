"""Write a Python program to read last two lines of a file. """

file = open("Vishal.txt", "r")
lines = file.readlines()    
print(lines[-2:])   
file.close()