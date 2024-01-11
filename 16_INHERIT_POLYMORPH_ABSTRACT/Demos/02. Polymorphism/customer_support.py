from employee import Employee


class CustomerSupport(Employee):
    def __init__(self, full_name, salary, department, email, phone_number):
        super().__init__(full_name, salary, department)
        self.email = email
        self.phone_number = phone_number

    # overridden
    def public_info(self):
        return f'{self.full_name}, Email: {self.email}, Phone: {self.phone_number}'
