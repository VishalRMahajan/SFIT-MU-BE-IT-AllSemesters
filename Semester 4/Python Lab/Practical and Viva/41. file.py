file = open("Vishal.txt", "w")
file.write("Hello, I am Vishal Mahajan SE-IT-A 63")
file.close()


file = open("Vishal.txt", "r")
print(file.read())
file.close()

file = open("Vishal.txt", "a")
file.write("\nI am learning Python")
file.close()

file = open("Vishal.txt", "r")
print(file.read())  
file.close()
