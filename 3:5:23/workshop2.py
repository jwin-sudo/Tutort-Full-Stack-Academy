def findThreeMax(n):
    max1 = n[0]
    max2 = n[0]
    max3 = n[0]
    for i in range(0, len(n), 1):
        if n[i] > n[0]:
            max3 = max2
            max2 = max1
            max1 = n[i]
        elif n[i] > max2:
            max3 = max2
            max2 = n[i]
        elif n[i] > max3:
            max3 = n[i]
    return max1, max2, max3


maxes = findThreeMax([15, 2, 7, 86, 0, 21, 50])
print(maxes)
