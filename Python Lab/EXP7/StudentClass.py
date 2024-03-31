"""Declare a Class with class-name Student which accepts the Student details, creates
an inner class of Student Marks with a constructor that takes marks as arguments and
returns the total and percentage of marks along with the student details"""


class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    class StudentMarks:
        def __init__(self, student, marks):
            self.student = student
            self.marks = marks

        def total(self):
            return sum(self.marks)

        def percentage(self):
            return (sum(self.marks) / len(self.marks))
        
        def display(self):
            print("\nStudent Details:")
            print("Name:", self.student.name)
            print("Roll No:", self.student.rollno)
            print("Marks:", self.marks)
            print("Total:", self.total())
            print("Percentage:", self.percentage())



name = input("\nEnter the name of the student:")
rollno = int(input("Enter the rollno of the student:"))

Student_obj = Student(name, rollno)


limit = int(input("\nEnter the number of subjects:"))


marks = []
for i in range(limit):
    marks.append(int(input("Enter the marks:")))
StudentMarks_obj = Student_obj.StudentMarks(Student_obj,marks)
StudentMarks_obj.display()


