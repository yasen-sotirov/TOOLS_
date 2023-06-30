import console_distionary as cd


def execute_instructions(line):
    command = line[0]
    new_word = line[1]

    if command == 'add':
        new_meaning = line[2]
        cd.add_word(new_word, new_meaning)

    elif command == 'update':
        new_meaning = line[2]
        cd.update_meaning(new_word, new_meaning)

    elif command == 'find':
        cd.find_word(new_word)
