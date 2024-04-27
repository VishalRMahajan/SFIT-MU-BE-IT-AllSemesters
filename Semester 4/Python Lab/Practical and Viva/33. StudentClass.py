class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    class StudentMarks:
        def __init__(self,student,marks,totalmarks):
            self.student = student
            self.marks = marks
            self.totalmarks = totalmarks

        def total(self):
            return sum(self.marks)
        
        def percentage(self):
            return (sum(self.marks)/self.totalmarks)*100
        
        def display(self):
            print("Name of Student is",self.student.name)
            print("Roll no of Student is",self.student.rollno)
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

totalmarks = int(input("Enter the Total Marks: "))
StudentMarks_obj = Student_obj.StudentMarks(Student_obj,marks,totalmarks)
StudentMarks_obj.display()
