maybe_number = input()

try:
    print('Trying to parse:')
    number = int(maybe_number)
except ValueError as ex:
    print(ex)
    print("You didn't enter a number")
except Exception:
    print("General exception")
except:
    print('I will catch everything!')
finally:
    print('Always executed')

print('Goodbye')
