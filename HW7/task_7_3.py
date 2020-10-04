def check_palindrome(list_of_words: list):
    number_of_palindromes = 0
    for word in list_of_words:
        if not isinstance(word, str):
            return 'List contains not only words'
        else:
            if word == word[::-1]:
                print(f'Палинромом является слово "{word}"')
                number_of_palindromes += 1
    return f'Количество палиндромов: {number_of_palindromes}'


list_of_words = ['шалаш', 'мороз', 'потоп']
print(check_palindrome(list_of_words))
