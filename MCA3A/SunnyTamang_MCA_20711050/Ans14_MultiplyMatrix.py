matrix1 = [
    [1, 3, 5],
    [2, 4, 6],
    [9, 7, 8]
]
matrix2 = [
    [3, 1, 5],
    [6, 7, 2],
    [8, 4, 9]
]
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

add = []
for i in range(len(matrix1)):
    for j in range(len(matrix[0])):
        for k in range(len(matrix2)):

            matrix[i][j] += matrix1[i][k] * matrix2[k][j]

for res in matrix:
    print(res)

# output
# [61, 42, 56]
# [78, 54, 72]
# [133, 90, 131]
