import keyword
import string

def is_valid_variable(name: str) -> bool:
    # Перевірка кількості нижніх підкреслень
    if name.count('_') > 1 and name.strip('_') == '':
        return False  # наприклад "__", "___"

    if name in keyword.kwlist:
        return False

    if not name:
        return False

    if name[0].isdigit():
        return False

    if any(c in string.punctuation.replace('_', '') for c in name):
        return False

    if any(c.isupper() for c in name):
        return False

    return True

# Приклади для тестування
test_cases = [
    "_", "__", "___", "x", "get_value", "get value",
    "get!value", "some_super_puper_value", "Get_value",
    "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"
]

for case in test_cases:
    print(f"{case}: {is_valid_variable(case)}")
