def addDigits(n):
    while n > 9:
        n = n % 10 + n//10
    return n


result = addDigits(138)
print(result)
