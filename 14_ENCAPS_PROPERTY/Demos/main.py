from employee import Employee
from employee_with_properties import EmployeeWithProperties


employee = Employee('Peter Griffin', 2000, 'Quality Control')

print(employee.salary)
employee.salary = -500
print(employee.internal_info())

employee_with_props = EmployeeWithProperties('Peter Griffin', 2000, 'Quality Control')

# we can read a 'read-only' property
print(employee_with_props.full_name)

# не може да променяме 'read-only' property-то, защото няма setter
# employee_with_props.full_name = 'Pesho Griffin'

# все пак ако решим, може да достигнем до self-a като напишем "_",
# но това по принцип intellisense -a не ни го дава като опция, пишем си го ръчно
employee_with_props._full_name = 'Pesho Griffin'
print(employee_with_props.full_name)

employee_with_props.salary = -500
print(employee_with_props.salary)
