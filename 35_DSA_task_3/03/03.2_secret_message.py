"Secret Message"  #
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
"""





from collections import deque

expression = "a3{bc2{be}f}jh"

open_d = []
close_d = []
multiplier = []

for ind in range(len(expression)):

    if expression[ind].isnumeric():
        multiplier.append(expression[ind])

    elif expression[ind] == "{":
        open_d.append(ind)

    elif expression[ind] == "}":
        close_d.append(ind)
