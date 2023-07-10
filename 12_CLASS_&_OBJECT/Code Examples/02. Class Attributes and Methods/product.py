class Product:

    # class attribute
    serial_number = 0

    @classmethod
    def next_serial(cls):
        cls.serial_number += 1
        return cls.serial_number

    def __init__(self, name, price):
        self.name = name
        self.price = price
        # call class method from the class
        self.serial = Product.next_serial() 

    def advertise(self):
        msg = f'Lovely {self.name} for only {self.price}!'
        return msg

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)

    def info(self):
        return f'SN: {self.serial} | {self.name} | {self.price }'
