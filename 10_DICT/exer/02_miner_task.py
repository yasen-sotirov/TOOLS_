"""
2.	A Miner Task
You will be given a sequence of strings, each on a new line until you receive
the "stop" command. Every odd line on the console represents a resource
(e.g., Gold, Silver, Copper, and so on) and every even - quantity.
Your task is to collect the resources and print them each on a new line.

Print the resources and their quantities in the following format:
"{resource} -> {quantity}"

Examples
Input
Gold
155
Silver
10
Copper
17
stop

Output
Gold -> 155
Silver -> 10
Copper -> 17

Input
gold
155
silver
10
copper
17
gold
15
stop

Output
gold -> 170
silver -> 10
copper -> 17
"""


command = input()
inventory = {}

while not command == "stop":
    metal = command
    quantity = int(input())

    # ако го няма го създавам
    if metal not in inventory:
        inventory[metal] = 0
    # ако го има го добавям
    inventory[metal] += quantity

    command = input()

for key, value in inventory.items():
    print(f'{key} -> {value}')

