"LOOP   WHILE, FOR"  # ЦИКЛИ

# for loop - expresion
# expresion = израз, който произвежда някаква стойност
# statemant = if/else  не връща стойност

"BREAK"     # приключи цикъла при допълнително условие
# i = 10
# while i > 0:
#     print(i)
#     if i == 5:
#         break
#     i -= 1


"CONTINUE"      # не изпълнява текущата итерация при определено условие
# for n in range(0, 10):
#     if n % 2 == 0:
#         continue
#     print(n)

# i = 10
# while i > 0:
#     i -= 1
#     if i % 2 == 0:
#         continue
#     print(i)


"RANGE СТЪПКА И ПОСОКА"
# for num in range(0, 10, 2):
#     print(num)

# for num in range(10, 0, - 2):
#     print(num)


"WHILE / ELSE:"     # когато while-a не е изпълнен влизаме в else:
# num = int(input())
# while num > 5:
#     num = int(input())
# else:
#     print("NUm < 5")


"ПИРАМИДА ОТ *"
# number = int(input())
#
# for index in range(1, number + 1):
#     print(index * '*')
# for i in range(number, 0, - 1):
#     print(i * "*")



"ПРИМЕР ИГРА"
# hidden_letter = "h"
# while True:
#     my_letter = input("guess a letter: ")
#     if hidden_letter == my_letter:
#         print("You guessed the letter")
#         break
#     elif hidden_letter > my_letter:
#         print("Hidden letter is after your letter")
#     else:
#         print("Hidden letter is before your letter")


x = 0
sequence = ''
while x <= 5:
    sequence += str(x) + " "
    x += 1
print(sequence)







