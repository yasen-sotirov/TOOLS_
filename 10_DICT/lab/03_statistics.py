"""" You will be receiving key-value pairs on separate lines separated by ": "
until you receive the command "statistics". Sometimes you may receive a product
more than once. In that case, you have to add the new quantity to the existing one.
When you receive the "statistics" command, print the following:
"Products in stock:
- {product1}: {quantity1}
- {product2}: {quantity2}
…
- {productN}: {quantityN}
Total Products: {count_all_products}
Total Quantity: {sum_all_quantities}"
"""


storage = {}
data = input()

while data != "statistics":
    product, quality = data.split(": ")
    # има ли го в речника речника
    if product not in storage:
        storage[product] = int(quality)
    else:
        storage[product] += int(quality)
    # завъртам цикъла
    data = input()

print("Products in stock:")
for key, value in storage.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(storage)}")
print(f"Total Quantity: {sum(storage.values())}")
