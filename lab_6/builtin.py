from functools import reduce

def multiply_list(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    else:
        return reduce(lambda x, y: x * y, numbers)

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

result = multiply_list(numbers)
if result is not None:
    print("Result of multiplying all numbers in the list:", result)
else:
    print("The list is empty.")
