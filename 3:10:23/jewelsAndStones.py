def jewelsAndStones(jewels, stones):
    lower = 0
    upper = 0
    for i in range(0, len(jewels), 1):
        for j in range(0, len(stones), 1):
            if jewels[i].islower() and jewels[i] in stones[j]:
                lower = lower + 1
            elif jewels[i].isupper() and jewels[i] in stones[j]:
                upper = upper + 1
    result = lower + upper
    return result


result = jewelsAndStones("z", "ZZ")
print(result)
