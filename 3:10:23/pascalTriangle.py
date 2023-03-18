def pascalTriangle(rowIndex):
    row = []
    row.append(1)

    for i in range(1, rowIndex, 1):
        for j in range(1, i, 1):
            row[j] = row[j-1] + row[j]
        row.append(1)
    return row


result = pascalTriangle(3)
print(result)
