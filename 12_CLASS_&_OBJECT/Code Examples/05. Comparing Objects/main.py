from product import Product
from product_equals import ProductWithEquals

cheese1 = Product('Cheese', 8.00)
cheese2 = Product('Cheese', 8.00)

# default: different ids == different objects
print(cheese1 == cheese2)
print(id(cheese1) == id(cheese2))

cheese3 = ProductWithEquals('Cheese', 8.00)
cheese4 = ProductWithEquals('Cheese', 8.00)

# defined __eq__: different ids and different objects, but 'structurally equal'  
print(cheese3 == cheese4)
print(id(cheese3) == id(cheese4))