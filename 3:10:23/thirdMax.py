def thirdMax(arr):
    max1 = min(arr)
    max2 = min(arr)
    max3 = min(arr)

    for i in range(0, len(arr)-1, 1):
        if arr[i] > max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max3 = max2
            max2 = arr[i]
        elif arr[i] > max3:
            max3 = arr[i]

    return max3


result = thirdMax([3, 2, 1])
print(result)
