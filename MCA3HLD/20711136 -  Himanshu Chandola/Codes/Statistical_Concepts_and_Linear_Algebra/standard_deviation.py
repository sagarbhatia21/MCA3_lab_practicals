# Himanshu Chandola MCA 3 - HLD Campus STD ID-20711136

observation = [11,15,14,12,10]
sum=0

for i in range(len(observation)):
    sum+=observation[i]

mean_of_observations = sum/len(observation)

sum_of_squared_deviation = 0

for i in range(len(observation)):

    sum_of_squared_deviation+=(observation[i]- mean_of_observations)**2
    Standard_Deviation = ((sum_of_squared_deviation)/len(observation))**0.5
    
print("Standard Deviation of sample is ",Standard_Deviation)