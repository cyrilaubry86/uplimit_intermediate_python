def evaluate(f, start, end):
    nums = [num for num in range(start, end) if num % 2 == 0] # choosing even numbers
    return f(nums)


def generate_squares(values):
    return [value**2 for value in values]


def generate_cubes(values):
    return [value**3 for value in values]


print(evaluate(f=generate_squares, start=0, end=10))
print(evaluate(f=generate_cubes, start=0, end=10))