
number = int(input("Ввести 4-х значне число:"))


num1 = number // 1000        # Перше значення
num2 = (number // 100) % 10  # Друге значення
num3 = (number // 10) % 10   # Третє значення
num4 = number % 10           # Четверте значення

# Виводимо цифри
print(num1)
print(num2)
print(num3)
print(num4)
