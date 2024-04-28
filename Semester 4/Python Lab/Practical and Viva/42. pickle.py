import pickle

class Student:
    def __init__(self):
        self.name = ""
        self.rollno = 0
        self.age = 0

    def getdata(self):
        self.name = input("Enter the Name of the Student: ")
        self.rollno = int(input("Enter the Roll No of the Student: "))
        self.age = int(input("Enter the Age of the Student: "))

    def display(self):
        print("Name: ", self.name)
        print("Roll number: ", self.rollno)
        print("Age: ", self.age)


student = Student()
student.getdata()

file = open("VishalPractical.pkl","wb")
pickle.dump(student,file)

file = open("VishalPractical.pkl","rb")
student = pickle.load(file)
student.display()
file.close()
