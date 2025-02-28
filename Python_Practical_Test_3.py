class Employee:
    employees = []
    def __init__(self,name,employee_id,salary,role,extra_info):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.role = role
        self.extra_info = extra_info
        Employee.employees.append(
            {'name': self.name, 'employee_id': self.employee_id, 'salary': self.salary, 'role': self.role,
             'extra_info': self.extra_info})

    def display_all_employees(self):
        print(Employee.employees)

    def filter_by_role(self, role):
        for employee in Employee.employees:
            if employee['role'] == role:
                print(employee)
            else:
                print(f"{role} not exists")

    def filter_by_salary(self, min_salary, max_salary):
        for employee in Employee.employees:
            if min_salary <= employee['salary'] <= max_salary:
                print(employee)



emp1 = Employee("Vansh",6060,7500,"Developer","Python")
emp1.display_all_employees()
emp1.filter_by_role("Developer")
emp1.filter_by_salary(7500,10000)



