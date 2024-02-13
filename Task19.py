def count_c(arr, a):
    count = 0
    for i in range(len(arr)):
        if arr[i] == a:
            count += 1
    return count

arr = [5, 6, 2, 2, 3, 3, 3, 5, 5, 5]
arr1 = [5, 6, 2, 2, 3, 3, 3, 5, 5, 5]
arr.sort(key = lambda l:count_c(arr1, l), reverse = True)
print(arr)