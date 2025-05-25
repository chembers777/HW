def multiply_digits_until_single_digit(n):
    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
    return n

print(multiply_digits_until_single_digit(999))   # 2
print(multiply_digits_until_single_digit(1000))  # 0
print(multiply_digits_until_single_digit(423))   # 8
print(multiply_digits_until_single_digit(33))    # 9
print(multiply_digits_until_single_digit(25))    # 0
print(multiply_digits_until_single_digit(1))     # 1
