# Himanshu Chandola MCA 3 - HLD Campus STD ID-20711136

print("ENTER THE ELEMENTS")
a = 2
b = 2
matrix = [[int(input("Enter the Element:"))for j in range(a)]for i in range(b)]


for i in range(a):
    for j in range(b):
         print(matrix[i][j], end=" ")
    print()


def determinant(m):
    h=m[0][0]
    i=m[0][1]
    j=m[1][0]
    k=m[1][1]
    det = (h*k)-(i*j)
    return det


def cofactor(k):
    A11= k[1][1]
    A12 =(-1)* k[1][0]
    A21 = (-1)*k[0][1]
    A22 = k[0][0]
    CFM = [[A11,A12],[A21,A22]]
    return CFM

d= determinant(matrix)
print("Determinant of the matrix is:",d)
if d==0:
    print("INVERSE OF THE MATRIX DOES NOT EXIST")
else:
    CM = cofactor(matrix) 
    print("The cofactor matrix is:")
    for i in range(a):
        for j in range(b):
             print(CM[i][j], end=" ")
        print()
    print()
    print("The adjoint of the matix is:")
    for j in range(a):
        for i in range(b):
             print(CM[i][j], end=" ")
        print()
    print()

    # Inverse of a matrix exists only if its determinant is not equal to 0.

    print("The inverse of matrix is:")
    for j in range(a):
        for i in range(b):
             print((1/d)*(CM[i][j]) , end=" ")
        print()