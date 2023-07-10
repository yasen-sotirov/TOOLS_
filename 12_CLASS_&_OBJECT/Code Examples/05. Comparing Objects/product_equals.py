class ProductWithEquals:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # magic method called by the comparison (==) operator
    def __eq__(self, other):
        # first check if 'other' is the correct class
        if not isinstance(other, ProductWithEquals):
            return False

        # then define how we compare objects of this class
        return (self.name == other.name
                and self.price == other.price)
