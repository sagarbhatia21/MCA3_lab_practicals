matrix1 = [
    [2, 4],
    [3, 6],
    [11, 2]
]

res = [
    [0, 0, 0],
    [0, 0, 0],
]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        res[j][i] = matrix1[i][j]

for r in res:
    print(r)


# # output
# [2, 3, 11]
# [4, 6, 2]
