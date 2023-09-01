"""
Cipher
In a warm, sunny day Andrew found a bottle near the sea. It was a very special bottle,
containing not one, but two messages. The first message contained a big sequence of digits (0-9).
“This must be a secret code”, Andrew thought. And he was right. After seeing the second message
everything became clearer. The second message said something like this: “A123C11B98”.
Another idea struck Andrew: “Hmm may be this is the cipher, used for creating the secret code”.
And again he was right.
An alphabetical message, containing only capital English letters, is encoded with the given cipher.
For every letter in the original message it is replaced by the given sequence of digits
in the cipher.
For example an original message ABC with a cipher A123C11B98 will be encoded as 1239811.
Write a program that for a given secret code from the first bottle message and a given cipher
from the second bottle message finds all possible original messages that can be encoded to the
given secret code.

    Input
Read from the standard input
On the first input line there will be the secret message (the sequence of digits)
On the second input line there will be the cipher used for encoding the message in
the given format: “{LetterX}{CodeForX}{LetterY}{CodeForY}…” where every LetterX from the
original message will be encoded with CodeForX in the secret code
One letter will have only one unique representation.
The input data will always be valid and in the format described. There is no need to
check it explicitly.

    Output
Print to the standard output
In the first console line you must print the number of all possible original messages
that can be encoded to the given secret code
On the next lines, print these messages, sorted alphabetically
See the examples bellow.

    Constraints
The given secret code will contain no more than 20 digits.
The cipher will be no longer than 180 symbols, containing only capital English letters and digits.
The number of original messages (the answers) will be no more than 2048.

    Input
1122
A1B12C11D2

    Output
3
AADD
ABD
CDD

    Input
778
Z123A7787X666Y234

    Output
0
"""
# from pip._vendor.rich.ansi import decoder

# МОЕТО - ДО КЪДЕТО ДОСТИГНАХ
# def check_cipher(string, code, dict_len):
#     edit_code = code
#     string = ""
#
#     if edit_code == "":
#         print(string)
#         return
#
#     for key, value in dictionary.items():
#         repetition = edit_code.count(value)
#         for _ in range(repetition):
#             if value in edit_code:
#                 string += key
#                 edit_code = edit_code.replace(value, "", 1)
#
#
#
#
#
#
# # 1122
# # A1B12C11D2
#
# message = input()
# cipher = input()
#
# dictionary = {}
# value_len = 0
# last_letter = 0
#
# for el in cipher:
#     if el.isalpha():
#         dictionary[el] = ""
#         last_letter = el
#     else:
#         dictionary[last_letter] += el
#
#
# d_len = len(dictionary)
#
# check_cipher("", message, d_len)


#  =============================
# РЕШЕНИЕ
import re
import collections

results = []
queue = collections.deque()
queue.append((
    '',  # nothing deciphered yet
    input()  # full code 'remaining'
))

# use capture groups to create a list of tuples
cypher = re.findall('([A-Z])([0-9]+)', input())

while queue:
    deciphered, remaining = queue.popleft()
    if not remaining:  # if all that's remaining is an empty string, we have a full match
        results.append(deciphered)
        continue

    # append all possible matches to the queue
    for letter, number in cypher:
        if remaining.startswith(number):
            queue.append((deciphered + letter,  # add the deciphered letter
                          remaining[len(number):]))  # remove the matched numbers

print(len(results))
print(*sorted(results), sep='\n')

#  =============================
#  OT EDO

encoded_message = "1122"
# A1B12C11D2

# cipher = {"A":1, "B":12, "C":11, "D": 2}

cipher = [("B", "12"), ("D", "2"), ("A", "1"), ("C", "11")]
cipher = sorted(cipher)
output = []


def decipher(encoded_mes: str, decoded_msg):
    if encoded_mes == "":
        output.append(decoded_msg)
    else:
        for ch, code in cipher:
            if encoded_mes.startswith(code):
                decipher(encoded_mes[len(code):], decoded_msg + ch)


decipher(encoded_message, "")

print(len(output))
print("\n".join(output))



