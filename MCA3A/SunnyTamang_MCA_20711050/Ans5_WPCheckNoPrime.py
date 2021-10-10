n = int(input("enter no: "))
flag = 0
m = 0

m = n/2

while (m > 0):
    if(n % 2 == 0):
        print("not a prime number")
        flag = 1
        break
    if(flag == 0):
        print("is a prime number")
    break
