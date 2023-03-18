def threeConsecutiveOdd(arr):
    counter = 0
    for i in range(0, len(arr)-1, 1):
        if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
            return True
        else:
            return False


check = threeConsecutiveOdd([2, 6, 4, 1])
print(check)
