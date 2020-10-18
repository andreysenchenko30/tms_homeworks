def reversed_arguments_decorator(some_func):
    def wrapper(*args):
        letters = list(*args)
        reversed_arguments = letters[::-1]
        some_func(reversed_arguments)
    return wrapper


@reversed_arguments_decorator
def phrase_from_letters(some_letters):
    phrase = ''
    for letter in some_letters:
        if not isinstance(letter, str):
            print('Wrong input')
        else:
            phrase += letter
    print(f'Перевернутая фраза: {phrase}')


phrase_from_letters(['П', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т'])
