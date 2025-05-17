def Index_sum(list):
    # Якщо список порожній, повертаємо 0
    if not list:
        return 0

    # Сума значень з парними індексами
    even_sum = sum(list[i] for i in range(0, len(list), 2))

    # Множимо суму на останній елемент
    result = even_sum * list[-1]
    return result

# Вивести списки
print(Index_sum([0, 1, 7, 2, 15, 5]))  # => 88
print(Index_sum([1, 3, 7]))  # => 30
print(Index_sum([3]))  # => 36
print(Index_sum([]))  # => 0
