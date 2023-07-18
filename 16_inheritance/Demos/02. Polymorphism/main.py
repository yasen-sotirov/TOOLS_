
from customer_support import CustomerSupport
from manager import Manager
from employee import Employee


company_employees = [
    Employee('Peter Griffin', 2000, 'Quality Control'),
    Manager('John Smith', 3000, 'Quality Control'),
    CustomerSupport('Tom Ford', 4000, 'Quality Control',
                    'tom@qc.com', '071238123')
]

for employee in company_employees:
    print(employee.public_info())