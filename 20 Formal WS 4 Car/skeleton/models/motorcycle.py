from models.vehicle import Vehicle

class Motorcycle(Vehicle):
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CATEGORY_LEN_MIN = 3
    CATEGORY_LEN_MAX = 10
    CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'

    WHEELS_COUNT = 2

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file


    def __init__(self, make: str, model: str, price: float, category_length: str):
        super().__init__(make, model, price)
        self.category = category_length
        self.comments = tuple()
        self.wheels_count = self.WHEELS_COUNT
        self.comments = tuple()


    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if len(value) < self.CATEGORY_LEN_MIN or len(value) > self.CATEGORY_LEN_MAX:
            raise ValueError(self.CATEGORY_LEN_ERR)
        self._category = value

    
    def string_returns(self):
        return f'\n'.join([
            'Motorcycle:',
            f'Make: {self.make}',
            f'Model: {self.model}',
            f'Wheels: 2',
            f'Price: ${self.price:.2f}',
            f'Category: {self.category}',
            '--NO COMMENTS--'
        ])



# motor_1 = Motorcycle("Yamaha", "Nov model", 500.00, "pistov")
# print(motor_1.price)
# print(motor_1.category)
# print(motor_1.make)
# print(motor_1.model)