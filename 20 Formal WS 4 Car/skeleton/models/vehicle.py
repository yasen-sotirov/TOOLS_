class Vehicle:
    def __init__(self, make: str, model: str, price: float):
        self.make = make
        self.model = model
        self.price = price


    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        if len(make) < self.MAKE_LEN_MIN or len(make) > self.MAKE_LEN_MAX:
            raise ValueError(self.MAKE_LEN_ERR)
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if len(model) < self.MODEL_LEN_MIN or len(model) > self.MODEL_LEN_MAX:
            raise ValueError(self.MODEL_LEN_ERR)
        self._model = model

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price < self.PRICE_MIN or price > self.PRICE_MAX:
            raise ValueError(self.PRICE_ERR)
        self._price = price


