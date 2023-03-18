def richestMan(accounts):
    m = sum(accounts[0])
    for i in accounts:
        m = max(m, sum(i))
    return m


result = richestMan([[1, 5], [7, 3], [3, 5]])
print(result)
