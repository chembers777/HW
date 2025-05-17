number = int(input("Ввести 5-е число:"))

# Прописуємо цифри з поділом та остачею
num1 = number % 10
num2 = (number // 10) % 10
num3 = (number // 100) % 10
num4 = (number // 1000) % 10
num5 = (number // 10000) % 10

# Перевертаємо число
u_num = (num1 * 10000 +
                   num2 * 1000 +
                   num3 * 100 +
                   num4 * 10 +
                   num5)

print("Перевернуте число:", u_num)
