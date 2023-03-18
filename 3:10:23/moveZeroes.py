def moveZeroes(arr):
    count = 0
    for i in range(0, len(arr), 1):
        if arr[i] != 0:
            arr[count] = arr[i]
            count = count + 1
    while count < len(arr):
        arr[count] = 0
        count = count + 1
    return arr


result = moveZeroes([0])
print(result)
