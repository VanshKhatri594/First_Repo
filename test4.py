# Given a dictionary where employees' names are keys and their monthly sales are values, determine:
#
# The employee with the highest sales.
#
# The top 3 employees sorted in descending order.

employee_sales = {
    "Alice": 5000,
    "Bob": 7500,
    "Charlie": 4200,
    "Diana": 9100,
    "Ethan": 6200
}

# Expected Output:
# Top Performer: Diana
# Top 3 Employees: [('Diana', 9100), ('Bob', 7500), ('Ethan', 6200)]


def max_sales(emp, sales):
    employee = {}
    for emp, sales in employee_sales.items():
        max_sales = employee.get(emp, 0)
        employee[emp] = max(sales, max_sales)
    return employee

top_performer = max(employee_sales, key=employee_sales.get)
print(f"Top Performer: {top_performer}")
print(f"Top 3 Employees: {sorted(employee_sales.items(), key=lambda x: x[1], reverse=True)[:3]}")