
def camel_case(words):
    text = words[0].lower()
    for i in range(1, len(words)):
        text += words[i].lower().capitalize()

    return text


def kebab_case(words):
    text = ''
    for word in words:
        text = f'{text}-{word.lower()}'

    return text.lstrip('-')
