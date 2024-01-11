"""
Longest Sequence of Equal
Write a program that finds the length of the maximal sequence of
equal elements in an array of N integers.
Input
    On the first line you will receive the number N
    On the next N lines the numbers of the array will be given

Output
    Print the length of the maximal sequence

Constraints
    1 <= N <= 1024

Sample tests
Input

10
2
1
1
2
3
3
2
2
2
1

Output
3
"""


number_n = int(input())
lst = []
index = 0

counter = 0
coincidences = []

# чете поредицата и слага в лист
for el in range(number_n):
    lst.append(int(input()))

# итерира през елементите на листа
for _ in range(len(lst) - 1):
    first_num = lst[index]
    second_num = lst[index + 1]
    if first_num == second_num:
        counter += 1

    # добавя постигнатия резултат и занулява брояча
    else:
        coincidences.append(counter + 1)
        counter = 0
    index += 1

max_coincidence = max(coincidences)
print(max_coincidence)



