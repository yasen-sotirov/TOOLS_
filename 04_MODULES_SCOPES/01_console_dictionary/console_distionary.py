
def add_word(word, meaning):
    console_dictionary.append([word, meaning])
    print(f'Added word "{word}"')


def update_meaning(word, new_meaning):
    is_found = False
    if not is_found:
        for element in console_dictionary:
            if element[0] == word:
                element[1] = new_meaning
                is_found = True
                print("Meaning updated")
            break
    else:
        print("No such word")


def find_word(word):
    is_found = False
    if not is_found:
        for element in console_dictionary:
            if element[0] == word:
                is_found = True
                print(f'{word}: {element[1]}')
            break
    else:
        print("No such word")


console_dictionary = []
