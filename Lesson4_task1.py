def move_zeros_to_end(list):
    # Залишаємо ненульові значення
    non_zero = [x for x in list if x != 0]
    # Додаємо нулі у кінець
    zeros = [0] * (len(list) - len(non_zero))
    # Вивести об'єднаний список
    return non_zero + zeros

# Виводимо списки
print(move_zeros_to_end([0, 1, 0, 12, 3]))      # => [1, 12, 3, 0, 0]
print(move_zeros_to_end([0]))                   # => [0]
print(move_zeros_to_end([1, 0, 13, 0, 0, 0, 5])) # => [1, 13, 5, 0, 0, 0, 0]
print(move_zeros_to_end([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))
