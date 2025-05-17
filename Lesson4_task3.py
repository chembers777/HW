import random

# Генерація списку з випадковою кількістю значень від 3 до 10
RandomList = [random.randint(1, 10) for _ in range(random.randint(3, 10))]

# Формуємо новий список: 1-й, 3-й і 2-й з кінця значень
if len(RandomList) >= 3:
    NewList = [RandomList[0], RandomList[2], RandomList[-2]]
else:
    NewList = RandomList  # Якщо менше 3-х елементів (хоча за умовою цього бути не може)

print("Випадковий список:", RandomList)
print("Новий список:", NewList)
