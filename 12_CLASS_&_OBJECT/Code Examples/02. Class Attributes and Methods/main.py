from product import Product

cheese = Product('Cheese', 8.00)
wine = Product('Wine', 12.50)

print(cheese.info())
print(wine.info())

# class attributes can be accessed from the class itself
print(Product.serial_number)
