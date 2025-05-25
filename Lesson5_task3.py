import string


def generate_hashtag(text):
    # Видаляємо пунктуацію та пробіли окрім літер і цифр
    cleaned = ''.join(char if char not in string.punctuation else ' ' for char in text)

    # Розбиваємо на слова, капіталізуємо, з'єднуємо
    words = cleaned.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = '#' + ''.join(capitalized_words)

    # Обрізаємо до 140 символів, якщо потрібно
    return hashtag[:140]


print(generate_hashtag('Python Community'))        # #PythonCommunity
print(generate_hashtag('i like python community!'))  # #ILikePythonCommunity
print(generate_hashtag('Should, I. subscribe? Yes!')) # #ShouldISubscribeYes
