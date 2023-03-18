def minAbsDifference(arr):
    arr.sort()
    min = abs(arr[1] - arr[0])
    new_arr = []

    for i in range(0, len(arr)-1, 1):
        if abs(arr[i+1] - arr[i]) <= min:
            min = abs(arr[i+1] - arr[i])
            new_arr.append([arr[i], arr[i+1]])
    return new_arr


result = minAbsDifference([4, 2, 1, 3])
print(result)
