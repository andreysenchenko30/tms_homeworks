def filter_decorator(some_func):
    def wrapper(*args):
        filtered_numbers = filter(lambda numbers: numbers % 2 == 1, list(*args))
        some_func(filtered_numbers)
    return wrapper


@filter_decorator
def multiplication(some_list):
    result_of_multiplication = 1
    for number in some_list:
        if not isinstance(number, int):
            print('Wrong input')
        else:
            if number % 3 == 0:
                result_of_multiplication *= number
    print(f'Произведение нечетных чисел, делящихся на 3: {result_of_multiplication}')


multiplication([1, 2, 3, 4, 5, 6, 9, 12])
