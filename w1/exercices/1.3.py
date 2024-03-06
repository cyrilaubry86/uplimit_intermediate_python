def generate_numbers(end, start=0):
  value = start
  while value < end:
    yield value
    value += 1
  
number_generator = generate_numbers(start=0, end=8)
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))