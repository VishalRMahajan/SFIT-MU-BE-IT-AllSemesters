"""Write a Python program to declare a base class College having two derived
classes student and faculty and display their details."""


class College:
    def __init__(self, name, dept, role):
        self.name = name
        self.dept = dept
        self.role = role

    def display(self):
        print("\nDetails:")
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Role:", self.role)


class Student(College):
    def __init__(self, name, dept, role, rollno):
        super().__init__(name, dept, role)
        self.rollno = rollno

    def display(self):
        super().display()
        print("Roll No:", self.rollno)

class Faculty(College):
    def __init__(self, name, dept, role, empid):
        super().__init__(name, dept, role)
        self.empid = empid

    def display(self):
        super().display()
        print("EmpID:", self.empid)


Studentobj = Student("Vishal", "IT", "Student", 63)
Studentobj.display()

Facultyobj = Faculty("Teacher", "IT", "Faculty", 221068)
Facultyobj.display()