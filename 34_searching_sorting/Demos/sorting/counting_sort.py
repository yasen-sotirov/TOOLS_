def counting_sort(arr: list[int]):
    min_e = min(arr) # this is just for memory efficiency
    max_e = max(arr)

    counter = [0] * (max_e - min_e + 1)
    for e in arr:
        # each element is used as index
        # we "count" how many times that element is seen
        counter[e - min_e] += 1

    start = 0
    for index, times_seen in enumerate(counter):
        while times_seen > 0:
            arr[start] = index + min_e
            times_seen -= 1
            start += 1




arr = [18, 11, 14, 15, 11, 12, 15, 13, 14, 13, 16, 17, 14, 11, 15, 10, 12, 19]
counting_sort(arr)
print(arr)
