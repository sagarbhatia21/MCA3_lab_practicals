# Himanshu Chandola MCA 3 - HLD Campus STD ID-20711136

test_str = 'GEHU is Good College'
print("The original string is : " + str(test_str))
  
lookp_dict = {"Good" : "very good", "College" : "College for MCA Students"}
  
temp = test_str.split()
res = []
for wrd in temp:
      
    res.append(lookp_dict.get(wrd, wrd))
      
res = ' '.join(res)
print("Replaced Strings : " + str(res)) 