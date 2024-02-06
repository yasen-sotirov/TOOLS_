from enum import Enum

class CheckLocation(Enum):
    SOFIA = "SOFIA"
    PLOVDIV = "PLOVDIV"
    VARNA = "VARNA"


line = input('Give me the location: ').upper()

try:
    if CheckLocation(line):
        print("da")
except ValueError:
    print("Location does not exist")

