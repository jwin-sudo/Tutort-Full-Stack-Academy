def findTheDifference(s, t):
    for i in range(0, len(t), 1):
        if t[i] not in s:
            return t[i]


result = findTheDifference("abcd", "abcde")
print(result)
