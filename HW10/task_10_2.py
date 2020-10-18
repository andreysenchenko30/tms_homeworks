from datetime import datetime


def time_decorator(some_func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        some_func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        return f'Время выполнения функции: {execution_time}'
    return wrapper


@time_decorator
def multiplication(some_list):
    result_of_multiplication = 1
    for number in some_list:
        if not isinstance(number, int):
            print('Wrong input')
        else:
            if number % 3 == 0:
                result_of_multiplication *= number
    print(f'Произведение чисел, делящихся на 3: {result_of_multiplication}')


print(multiplication([1, 2, 3, 4, 5, 6, 9, 12]))
