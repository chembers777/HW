import string

def letters_range(input_str):
    all_letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    start, end = input_str.split('-')
    start_index = all_letters.index(start)
    end_index = all_letters.index(end)
    return all_letters[start_index:end_index + 1]


print(letters_range("a-c"))  # abc
print(letters_range("a-a"))  # a
print(letters_range("s-H"))  # stuvwxyzABCDEFGH
print(letters_range("a-A"))  # abcdefghijklmnopqrstuvwxyzA
