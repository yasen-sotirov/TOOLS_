"Secret Message" #
"""
You want to exchange some secret messages between you and your friends, 
so you decide to encode them using a simple but yet powerful rule: 
n{encoded_text}, where the encoded_text in the curly brackets is 
repeated exactly n times.

Your job is to write a program which decodes the messages. 
Examine the sample tests below.

Input
    Read from the standard input
    On the single line you will find the encoded message

Output
    Print to the standard output
    On the single line print the decoded message

Constraints
    1 <= n <= 100
    encoded_text contains only small letters from "a" to "z"


    Input
4{a}2{xz}

    Output
aaaaxzxz

    Input
2{z10{xy}}

    Output
zxyxyxyxyxyxyxyxyxyxyzxyxyxyxyxyxyxyxyxyxy


    Input
a3{cd2{a}f}ef

    Output
acdaafcdaafcdaafef

    Input
a2{bc2{d}e}fj

    Output
abcddebcddefj
"""
from collections import deque

input_str = "a2{bc2{d}e}fj"        #input()
result_stack = []
while input_str:
    open_stack = []
    close_queue = deque()
    multiplier_stack = []

    for index in range(len(input_str)):
        el = input_str[index]
        if el == "{":
            open_stack.append(index)
        elif el == "}":
            close_queue.append(index)
        elif el.isnumeric():
            multiplier_stack.append(el)
    if open_stack:
        open_par = open_stack.pop()
        clos_par = close_queue.popleft()
        multiplier = int(multiplier_stack.pop())
        letter_group = ""

        for letter in input_str[open_par:clos_par]:
            if letter.isalpha():
                letter_group += letter
        result_stack.append(letter_group * multiplier)
        input_str = input_str[:open_par - 1] + input_str[clos_par + 1:]

    else:
        for _ in range(len(result_stack)):
            el = result_stack.pop()
            print(el, end="")



