def count_chet(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == min(arr):
            count += 1
    return count

arr = [1, 2, 3, 4, 5]
print(count_chet(arr))