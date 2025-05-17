def split_list(list):
    # Знаходимо середину списку (більшу частину, якщо непарна)
    mid = (len(list) + 1) // 2

    # Ділимо список на дві частини
    FirstHalf = list[:mid]
    SecondHalf = list[mid:]

    # Повертаємо новий список з двох списків
    return [FirstHalf, SecondHalf]

# Вивести списки
print(split_list([1, 2, 3, 4, 5, 6]))   # => [[1, 2, 3], [4, 5, 6]]
print(split_list([1, 2, 3]))            # => [[1, 2], [3]]
print(split_list([1, 2, 3, 4, 5]))      # => [[1, 2, 3], [4, 5]]
print(split_list([1]))                  # => [[1], []]
print(split_list([]))                   # => [[], []]
