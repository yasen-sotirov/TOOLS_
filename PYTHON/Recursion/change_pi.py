def change(data):
    if len(data) < 2:
        return data

    if data[:2] == "pi":
        return "3.14" + change(data[2:])

    return data[0] + change(data[1:])

print(change(input()))

# xpixxpix