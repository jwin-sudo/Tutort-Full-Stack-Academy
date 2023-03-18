def sumArray(arr):
    sum = 0
    for i in range(0, len(arr), 1):
        sum = sum + arr[i]
        arr[i] = sum
    return arr


result = sumArray([1, 1, 1, 1, 1])
print(result)
