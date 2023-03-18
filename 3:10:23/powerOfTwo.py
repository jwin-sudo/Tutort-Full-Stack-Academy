
def powerOfTwo(n):
    for i in range(0, 32, 1):
        if pow(2, i) == n:
            return True
    return False


result = powerOfTwo(8)
print(result)
