def insertion_sort(arr: list[int]):
    # start at i=1 - we assume that i=0 is in position
    for i in range(1, len(arr)):
        to_insert = arr[i] 
        j = i - 1

        # search BACKWARDS to find the place for insertion
        # in the process, move all larger elements one position to the right
        while j >= 0 and arr[j] > to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        
        # perform the "insertion"
        arr[j + 1] = to_insert


arr = [8, 1, 4, 5, 1, 2, 5, 3, 4, 3, 6, 7, 4, 1, 5, 0, 2, 9]
insertion_sort(arr)
print(arr)
