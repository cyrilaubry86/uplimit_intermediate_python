# reduce(function, iterable, [initial value])

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
add_func = lambda accumulator, current_value: accumulator + current_value


print(reduce(add_func, numbers))
print(reduce(add_func, numbers, 5))
