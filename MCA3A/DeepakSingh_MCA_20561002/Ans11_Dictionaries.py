Dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(Dict)

Dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: {'e', 'f'}}
print(Dict)

# value gets updated of Index 0 and 1
Dict[0] = 'user'
Dict[1] = 'admin'

print(Dict)
