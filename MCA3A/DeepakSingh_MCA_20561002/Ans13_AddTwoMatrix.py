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

add = []
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        add.append(matrix1[i][j] + matrix2[i][j])
print(add)

# output
# [4, 4, 10, 8, 11, 8, 17, 11, 17]
