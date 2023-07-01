"""
Find Average
You need to calculate the average of a collection of values. Every value will be valid number. The average must be printed with two digits after the decimal point.
Input
    On the first line, you will receive N - the number of the values you must read
    On the next N lines you will receive numbers.
Output
    On the only line of output, print the average with two digits after the decimal point.
Input

4
1
1
1
1

Output
1.00


Input
3
2.5
1.25
3

Output
2.25

"""


num = int(input())
sum_num = 0

for _ in range(num):
    current_num = float(input())
    sum_num += current_num

print(f'{sum_num / num:.2f}')
