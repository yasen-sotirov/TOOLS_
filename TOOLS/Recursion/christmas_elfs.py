def delivery(lst):
    if len(lst) == 1:
        print(f"deliver to {lst[0]}")

    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        delivery(left)
        delivery(right)

child = ["Ivan", "Pesho", "Tosho", "Gosho", "Ginka", "Stamat", "Gertruda", "Kalinka"]
delivery(child)