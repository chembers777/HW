def seconds_to_readable_time(seconds):
    days, rem = divmod(seconds, 86400)  # 86400 секунд у добі
    hours, rem = divmod(rem, 3600)      # 3600 секунд у годині
    minutes, secs = divmod(rem, 60)     # 60 секунд у хвилині

    # Вибір правильної форми слова "день"
    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
        day_word = "дні"
    else:
        day_word = "днів"

    # Форматування з провідними нулями
    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}"

    return f"{days} {day_word}, {time_str}"

print(seconds_to_readable_time(0))         # 0 днів - 00:00:00
print(seconds_to_readable_time(224930))    # 2 дні - 14:28:50
print(seconds_to_readable_time(466289))    # 5 днів - 09:31:29
print(seconds_to_readable_time(950400))    # 11 днів - 00:00:00
print(seconds_to_readable_time(1209600))   # 14 днів - 00:00:00
print(seconds_to_readable_time(1900800))   # 22 дні - 00:00:00
print(seconds_to_readable_time(8639999))   # 99 днів - 23:59:59
print(seconds_to_readable_time(22493))     # 0 днів - 06:14:53
print(seconds_to_readable_time(7948799))   # 91 день - 23:59:59
