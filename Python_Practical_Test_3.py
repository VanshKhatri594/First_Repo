class Employee:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        n = int(input("Enter the number of employees you want to add: "))
        for i in range(n):
            name = input("Enter the name of the employee: ")
            emp_id = int(input("Enter the employee ID: "))
            salary = int(input("Enter the salary of the employee: "))
            role = input("Enter the role of the employee: ")
            other_info = input("Enter other information of the employee: ")
            self.employees.append({'name': name, 'emp_id': emp_id, 'salary': salary,
                                   'role': role, 'other_info': other_info})

    def display_employee(self):
        if not self.employees:
            print("No employees available.")
        else:
            for emp in self.employees:
                print(emp)

    def filter_by_role(self, role):
        found = False
        for emp in self.employees:
            if emp['role'].lower() == role.lower():
                print(emp)
                found = True
        if not found:
            print(f"No employees found with role '{role}'.")

    def filter_by_salary(self, min_salary, max_salary):
        found = False
        for emp in self.employees:
            if min_salary <= emp['salary'] <= max_salary:
                print(emp)
                found = True
        if not found:
            print(f"No employees found with salary between {min_salary} and {max_salary}.")


emp = Employee()

while True:
    options = input('1. Add Employee, 2. Filter by Role, 3. Filter by Salary, 4. Display Employees, 5. Exit: ')

    if options == '1':
        emp.add_employee()
    elif options == '2':
        role = input("Enter the role you want to filter: ")
        emp.filter_by_role(role)
    elif options == '3':
        min_salary = int(input("Enter the minimum salary: "))
        max_salary = int(input("Enter the maximum salary: "))
        emp.filter_by_salary(min_salary, max_salary)
    elif options == '4':
        emp.display_employee()
    elif options == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid option. Please try again.")
