def get_word():
    print('Enter the secret word: ')
    word = input()
    return word.lower()


def get_initial_positions(length):
    return [True, *([False] * (length - 2)), True]


def check_guess(word, letter, positions):
    new_positions = positions.copy()
    letter = letter.lower()
    for i in range(len(word)):
        if word[i] == letter:
            new_positions[i] = True

    return new_positions


def hide_word(word, positions):
    hidden = ''
    for i in range(len(word)):
        if positions[i]:
            hidden += word[i]
        else:
            hidden += '-'

    return hidden


def check_for_win(positions):
    for p in positions:
        if p == False:
            return False

    return True


def play_hangman():
    word = get_word()
    lives = 5
    positions = get_initial_positions(len(word))
    print(hide_word(word, positions))

    while True:
        next_letter = input()
        new_positions = check_guess(word, next_letter, positions)

        if new_positions == positions:
            print('No such letter or already guessed')
            print(f'Lives remaining: {lives - 1}')
            lives = lives - 1
            if lives == 0:
                print('You lose!')
                break

        # option 2:
        elif check_for_win(new_positions):
            print('You win!')
            break
        else:
            print('Another letter guessed!')
            print(hide_word(word, new_positions))
            positions = new_positions
