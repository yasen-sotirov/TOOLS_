def sum_pairs(numbers):
    for num in numbers:
        print(num)

    for n1 in numbers:
        for n2 in numbers:
            if n1 != n2:
                sum = n1 + n2
                print(sum)


sum_pairs([1,1,1,1,1,1,1])
sum_pairs([1,2,3,4,5,6,7])