def LastToFirst(list):
    # Якщо список порожній то повертаємо його без змін
    if not list:
        return list

    # Переміщуємо останнє значення на початок
    return [list[-1]] + list[:-1]

# Вивід
print(LastToFirst([12, 3, 4, 10]))       # => [10, 12, 3, 4]
print(LastToFirst([1]))                  # => [1]
print(LastToFirst([]))                   # => []
print(LastToFirst([12, 3, 4, 10, 8]))    # => [8, 12, 3, 4, 10]
