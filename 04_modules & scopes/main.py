import questions
import game_functions

print(questions.question_1)

for index in range(len(questions.question_1_answer)):
    answer = questions.question_1_answer[index]
    letter = game_functions.get_letters(index)
    print(f'{letter}. {answer}')

my_answer = input("Your answer? (A, B, C, D)")

if my_answer == questions.question_1_correct:
    print("Correct")
else:
    print('incorrect')