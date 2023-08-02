
print('Before loop')

maybe_number = input()
val = int(maybe_number)


iterations = input()

# runtime error
for _ in range(iterations):
    print('In loop')

print('After loop')