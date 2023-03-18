def reverseVowels(s):
    arr = ['a', 'e', 'i', 'o', 'u']
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] not in arr:
            left = left + 1
        if s[right] not in arr:
            right = right - 1
        s[left], s[right] = s[right], s[left]
    return s


result = reverseVowels('hello')
print(result)
