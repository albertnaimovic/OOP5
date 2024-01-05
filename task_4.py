# Task Nr.4:

# Create a class called Employee with a static method called calculate_payroll that takes a list of Employee instances
# and returns the total amount to be paid to all employees. Each Employee instance has two attributes: name and salary.


from typing import List


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_payroll(employee_list: List["Employee"]) -> float:
        salary_list = [employee.salary for employee in employee_list]
        return sum(salary_list)


employee1 = Employee(name="Jonas", salary=1500)
employee2 = Employee(name="Diana", salary=600)
employee3 = Employee(name="Agne", salary=700)
employee4 = Employee(name="Darius", salary=2000)
employee5 = Employee(name="Paulius", salary=1600)
employee_list = [employee1, employee2, employee3, employee4, employee5]

print(Employee.calculate_payroll(employee_list))
