numbers = input("Введите список чисел через пробел: ").split()
numbers.sort(reverse=True)
numbers_as_strings = [str(num) for num in numbers]
result = "".join(numbers_as_strings)
print("Максимально возможное число:", result)
