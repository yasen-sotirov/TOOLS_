from collections import defaultdict

data = input().split()
unique_words = []

word_dict = defaultdict(list)

for word in data:
    sorted_word = ''.join(sorted(word))
    word_dict[sorted_word].append(word)

for anagram_group in word_dict.values():
    unique_words.append(anagram_group[0])

print(' '.join(unique_words))




"""# nap teachers cheaters pan ear era hectares
data = input().split()
output = []


while data:
    word = data.pop(0)
    for el in data:
        if len(word) == len(el):
            el_list = [x for x in el]
            word_list = [y for y in word]

            for index in range(len(el_list)):
                letter = el_list[0]
                if letter in word_list:
                    word_list.remove(letter)
                    el_list.remove(letter)

            if not el_list and not word_list:
                output.append(word)
                data.remove(el)
                break

print(" ".join(output))
"""