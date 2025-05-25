while True:
    # Перше число
    num1 = float(input("Введіть перше число: "))

    # Математична дія
    operation = input("Введіть дію (+, -, *, /): ")

    # Друге число
    num2 = float(input("Введіть друге число: "))

    # Обчислення
    if operation == '+':
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")
        else:
            print("Помилка: ділення на нуль")
    else:
        print("Помилка: невідома математична дія!")

    # Запит на продовження
    cont = input("Бажаєте продовжити? (y/yes для продовження): ").strip().lower()
    if cont not in ['y', 'yes']:
        print("Завершення роботи калькулятора.")
        break
