import random

# Генерація списку від 3 до 10 значень з чисел від 1 до 500
RandomList = [random.randint(1, 500) for _ in range(random.randint(3, 10))]

# Новий список з 1-го, 3-го і 2-го з кінця значень
NewList = [RandomList[0], RandomList[2], RandomList[-2]]

print(f"Перший список: {RandomList}")
print(f"Новий список: {NewList}")
