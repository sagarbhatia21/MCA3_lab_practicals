# Himanshu Chandola MCA 3 - HLD Campus STD ID-20711136

print("Enter the Number of which you want to find factorial: ")
num = int(input())

fact = 1
i = 1
while i<=num:
    fact = fact*i
    i = i+1

print("\nFactorial of given number is =", fact)