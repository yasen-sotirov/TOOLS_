"""
Special words

Anagrams are words that have the same number of same letters,
but in different order
    For instance:
    nap - pan
    ear - are - era
    cheaters - hectares - teachers

Write a program that gets words from the input and returns only the
unique ones without the anagrams.
Input
    The input consists of one line only, which contains the words,
    separated by space.
Output
    Output a single line - print all unique words without the
    anagrams separated by space. You should select only the first
    word from the words with the same anagram.

Constraints

1 <= words count <= 100
Sample Tests
Input
nap teachers cheaters pan ear era hectares

Output
nap teachers ear

Input
rat tar art

Output
rat
"""

def is_new(word: str, cache: set[str] = set()):
    anagram = ''.join(sorted(word.lower()))

    if anagram in cache:
        return False

    else:
        cache.add(anagram)
        return True


print(*(w for w in input().split() if is_new(w)))