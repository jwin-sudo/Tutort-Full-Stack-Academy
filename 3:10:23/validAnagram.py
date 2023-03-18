def validAnagram(s, t):
    
    for i in range(0, len(s), 1):
        for j in range(0, len(t), 1):
            if s[i] in t[j]:
                return True
            else:
                return False


result = validAnagram("anagram", "nagaram")
print(result)
