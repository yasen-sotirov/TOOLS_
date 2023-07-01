num = int(input())

for index in range(1, num + 1):
    if index % 3 == 0 or index % 7 == 0:
        continue
    print(index, end=" ")
