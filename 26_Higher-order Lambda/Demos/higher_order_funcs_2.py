
def console_output(value: str) -> None:
    print(value)


def file_output(value: str) -> None:
    with open('output_file.txt', mode='w') as f:
        f.write(value)


def create_output(output_func):
    data = [
        'This is my very important data',
        'It will be saved wherever the output_func decides.'
    ]

    output_func('\n'.join(data))


create_output(console_output)
create_output(file_output)
