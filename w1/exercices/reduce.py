from functools import reduce
values = [2, 3, 4, 7, 10, 21]

print(reduce(lambda x, y: x+y, values)) # sum of all values in a list
print(reduce(lambda x, y: x*y, values)) # product of all values in a list
