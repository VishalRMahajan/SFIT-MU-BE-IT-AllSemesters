"""Create a class Student to input data members roll number, name, age with a display method to print their details,using pickle module. """


import pickle

class Student:
    def __init__(self):
        self.roll = 0
        self.name = ""
        self.age = 0

    def getdata(self):
        self.roll = int(input("Enter the roll number: "))
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))

    def display(self):
        print("Roll number: ", self.roll)
        print("Name: ", self.name)
        print("Age: ", self.age)    


s = Student()

s.getdata()

file = open("Student.pkl", "wb")
pickle.dump(s, file)
file.close()


print("\nReading from file")
file = open("Student.pkl", "rb")
s = pickle.load(file)
s.display()
file.close()
