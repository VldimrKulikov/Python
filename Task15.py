def cyclic_shift(arr):
    arr[:] = arr[len(arr) - 2:] + arr[:len(arr) - 2]
    return arr


arr = [1, 2, 3, 4, 5]
result = cyclic_shift(arr)
print(result)