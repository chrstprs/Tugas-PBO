# Contoh kode functional programming

def multiply_by_two(numbers):
    return list(map(lambda x: x * 2, numbers))

numbers = [1, 2, 3, 4, 5]
result = multiply_by_two(numbers)
print(result)