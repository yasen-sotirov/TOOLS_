from models.vehicle import Vehicle


class Car(Vehicle):
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CAR_SEATS_MIN = 1
    CAR_SEATS_MAX = 10
    CAR_SEATS_ERR = f'Seats must be between {CAR_SEATS_MIN} and {CAR_SEATS_MAX}!'

    WHEELS_COUNT = 4

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
    
    
    def __init__(self, make: str, model: str, price: float, seats: int):
        super().__init__(make, model, price)
        self.seats = seats
        self.comments = tuple()
        self.wheels_count = self.WHEELS_COUNT


    @property
    def seats(self):
        return self._seats
    
    @seats.setter
    def seats(self, value):
        if value < self.CAR_SEATS_MIN or value > self.CAR_SEATS_MAX:
            raise ValueError(self.CAR_SEATS_ERR)
        self._seats = value    



    def string_returns(self):
        return f'\n'.join([
            'Car:',
            f'Make: {self.make}',
            f'Model: {self.model}',
            f'Wheels: {self.wheels_count}',
            f'Price: ${self.price:.2f}',
            f'Seats: {self.seats}',
            '--NO COMMENTS--'
        ])

# car_1 = Car("Toyota", "Raw 4", 10000.00, 5)
# print(car_1.price)
# print(car_1.seats_count)
# print(car_1.make)
# print(car_1.model)