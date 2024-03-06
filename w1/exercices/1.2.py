def generate_numbers(end, start=0):
  value = start
  while value < end:
    yield value
    value += 1
  
number_generator =  generate_numbers(10, start=0)
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))
print(next(number_generator))