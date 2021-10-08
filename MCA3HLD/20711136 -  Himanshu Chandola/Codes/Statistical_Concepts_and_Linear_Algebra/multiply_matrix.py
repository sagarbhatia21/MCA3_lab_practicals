# Himanshu Chandola MCA 3 - HLD Campus STD ID-20711136

arr1=[[0,0,0],[0,0,0],[0,0,0]]
arr2=[[0,0,0],[0,0,0],[0,0,0]]
arr3= [[0,0,0],[0,0,0],[0,0,0]]

print("Enter the Elements of Array 1:")
for i in range(0,3):
    for j in range(0,3):
        element= int(input())
        arr1[i][j]=element

print("Enter the Elements of Array 2:")
for i in range(3):
    for j in range(3):
        element2= int(input())
        arr2[i][j]=element2

for i in range(3):
    for j in range(3):
        for k in range(3):
            arr3[i][j]+=arr1[i][k]*arr2[k][j]
                                               
print(arr3[0],'\n',arr3[1],'\n',arr3[2])