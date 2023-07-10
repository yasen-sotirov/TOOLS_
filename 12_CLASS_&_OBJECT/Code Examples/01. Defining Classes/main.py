from product import Product

cheese = Product('Cheese', 8.00)
wine = Product('Wine', 12.50)

print(cheese.advertise())
print(wine.advertise())

cheese.apply_discount(20)
print(cheese.advertise())
