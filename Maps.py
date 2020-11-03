# Python Maps also called ChainMap is a type of data structure to manage multiple dictionaries together as one unit.
# The combined dictionary contains the key and value pairs in a specific sequence eliminating any duplicate keys.
# The best use of ChainMap is to search through multiple dictionaries at a time and get the proper key-value pair mapping.
# We also see that these ChainMaps behave as stack data structure.

import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)
print(res.maps, '\n')

print('Keys = {}'.format(list(res.keys())))
print('Value = {}'.format(list(res.values())))

# print all elements from result
print('elements')
for key, val in res.items():
    print('{} = {}'.format(key, val))

# find a specific key in map
print('day3 in res: {}'.format(('day1' in res)))

# Map Reordering
# If we change the order the dictionaries while clubbing them in the above example we see that the position of the elements get interchanged
# as if they are in a continuous chain. This again shows the behaviour of Maps as stacks.
res1 = collections.ChainMap(dict1, dict2)

print(res1.maps, '\n')

res2 = collections.ChainMap(dict2, dict1)

print(res2.maps, '\n')

# Updating Map
# When the element of the dictionary is updated, the result is instantly updated in the result of the ChainMap.
# In the below example we see that the new updated value reflects in the result without explicitly applying the ChainMap method again.
res = collections.ChainMap(dict1, dict2)

print(res.maps, '\n')

dict2['day4'] = 'Fri'

print(res.maps, '\n')
