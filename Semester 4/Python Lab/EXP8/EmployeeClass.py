"""Write a menu driven program to demonstrate OOP in python.
● Create a class Employee with following attribute as EmpID, name, dept, and
salary
● Print name: ,%s and salary:, %10.2f when an object is printed.
● Create a function to update the salary of a given employee. Print the total number of
employees.
● Create two derived classes “Manager” and “Staff” from base class “Employee” and
display their details."""

class Employee:
    total_employees = 0
    def __init__(self, EmpID, name, dept, salary,role):
        self.EmpID = EmpID
        self.name = name
        self.dept = dept
        self.salary = salary
        self.role = role
        Employee.total_employees += 1

    def __str__(self):
        return "Name: %s, Salary: %10.2f" % (self.name, self.salary)

    def update_salary(self, salary):
        self.salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("EmpID:", self.EmpID)
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Salary:", self.salary)
        print("Role:", self.role)

    def total(self):
        print("\nTotal number of employees:", Employee.total_employees)


class Manager(Employee):
    def __init__(self, EmpID, name, dept, salary,role):
        super().__init__(EmpID, name, dept, salary,role)
        
    def display(self):
        super().display()


class Staff(Employee):
    def __init__(self, EmpID, name, dept, salary,role):
        super().__init__(EmpID, name, dept, salary,role)
        
    def display(self):
        super().display()




def main():
    employees = []

    while True:
        print("\n1. Add Staff")
        print("2. Add Manager")
        print("3. Display Staff/Manager Details")
        print("4. Update Salary")
        print("5. Display Total Employees")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            EmpID = input("Enter Staff ID: ")
            name = input("Enter Staff Name: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            employees.append(Staff(EmpID, name, dept, salary,role="Staff"))

        elif choice == 2:
            EmpID = input("Enter Manager ID: ")
            name = input("Enter Manager Name: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            employees.append(Manager(EmpID, name, dept, salary,role="Manager"))

        elif choice == 3:
            for employee in employees:
                employee.display()

        elif choice == 4:
            EmpID = input("Enter Employee ID to Update Salary: ")
            salary = float(input("Enter New Salary: "))
            for employee in employees:
                if employee.EmpID == EmpID:
                    employee.update_salary(salary)
                    print("Salary updated successfully.")
                    break
            else:
                print("Employee ID not found.")

        elif choice == 5:
            print("\nTotal number of employees:", Employee.total_employees)

        elif choice == 6:
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()