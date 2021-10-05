# Himanshu Chandola MCA 3 - HLD Campus STD ID-20711136

n_num = [11, 12, 13, 14, 15]
n = len(n_num)
n_num.sort()
  
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))