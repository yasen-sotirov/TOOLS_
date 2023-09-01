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
"""

# a2{bc2{d}e}f

def recursion(sequence, multiplier, ):
    letters = ""

    for index, el in enumerate(sequence):
        element = el

        if el.isnumeric():
            recursion(sequence[index + 2:], int(el))

        elif el.isalpha():
            letters += el

        elif el == "}":
            return letters * multiplier


print(recursion("a2{bc2{d}e}fg", 1))

# expected output:  abcddebcddefg




def recursion(sequence, multiplier):
    letters = ""

    i = 0
    while i < len(sequence):
        if sequence[i].isnumeric():
            j = i + 1
            while sequence[j].isnumeric():
                j += 1
            inner_multiplier = int(sequence[i:j])
            inner_result, consumed_chars = recursion(sequence[j + 1:], inner_multiplier)
            letters += inner_result
            i = j + consumed_chars + 2
        elif sequence[i].isalpha():
            letters += sequence[i]
            i += 1
        elif sequence[i] == "}":
            return letters, i
        else:
            i += 1

    return letters * multiplier, len(sequence)

result, _ = recursion("a2{bc2{d}e}fg", 1)
print(result)
