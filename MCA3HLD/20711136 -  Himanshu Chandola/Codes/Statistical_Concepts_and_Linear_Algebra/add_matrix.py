# Himanshu Chandola MCA 3 - HLD Campus STD ID-20711136

a = []
b = [] 
c = [] 
print("Enter First Matrix : ")
for i in range(3):
    d = []
    for j in range(3):
	    d.append(int(input())) 
    a.append(d) 
print("Enter Second Matrix:")
for i in range(3):
    d = []
    for j in range(3):
	    d.append(int(input())) 
    b.append(d)
print("The First Matrix is: ")
for i in range(3):
	for j in range(3):
		print(a[i][j],end=" ")
	print("")
print("The Second Matrix is : ")
for i in range(3):
	for j in range(3):
		print(b[i][j],end=" ")
	print("")
for i in range(3):
    d = []
    for j in range(3):
	    d.append(int(a[i][j] + b[i][j]))
    c.append(d)
print("Addition Of Two Matrices :");
for i in range(3):
	for j in range(3):
		print(c[i][j] ,end=" ")
	print("")