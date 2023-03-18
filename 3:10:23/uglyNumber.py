def uglyNumber(n):
    arr = [2, 3, 5]
    isUgly = True

    if n < 1:
        isUgly = False
    if n == 1:
        isUgly = True
    for i in range(2, n, 1):
        if n % i == 0 and i not in arr:
            return False
    return True


result = uglyNumber(14)
print(result)
