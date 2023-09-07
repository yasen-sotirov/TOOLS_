def change(data):
    if len(data) <= 2:
        return data

    if data[:2] == "hi":
        return "3.14" + change(data[2:])
    return change(data[1:])

print(change(input()))
