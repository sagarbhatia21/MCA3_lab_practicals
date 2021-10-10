# n = int(input("Enter the value of 'n': "))
# a = 0
# b = 1
# sum = 0
# count = 1
# while(count <= n):
#     a = b
#     b = sum
#     sum = a + b
#     count += 1
#     print(sum)


# using functool
def fibo(n):
    a = 0
    b = 1

    for i in range(n):
        c = a+b
        a = b
        b = c
    print(c, end=" ")


fibo(10)
