
from customer_support import CustomerSupport
from manager import Manager
from employee import Employee


employee = Employee('Peter Griffin', 2000, 'Quality Control')
manager = Manager('John Smith', 2000, 'Quality Control')
customer_support = CustomerSupport('Gregory House', 2000, 'Quality Control', 'gregory@qc.company', '071238123')

# inherited attributes and methods
print(manager.public_info())
print(manager.internal_info())
print(manager.salary)
print(customer_support.public_info())
print(customer_support.internal_info())
print(customer_support.salary)

# Manager-only attributes and methods
manager.add_employee(employee)
manager.add_employee(customer_support)
print(len(manager.employees))

# CustomerSupport-only attributes and methods
print(customer_support.phone_number)
print(customer_support.contacts())
