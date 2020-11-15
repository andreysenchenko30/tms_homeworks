def wrapper_function(some_func):
    some_dict = {}

    def wrapper(*args):
        for i in args:
            number = int(i)
            if not number in some_dict:
                a = number
                b = some_func(number)
                some_dict[a] = b
                print(b)
            else:
                print(some_dict[number])
                print('Returned from dict')
    return wrapper


@wrapper_function
def some(a):
    b = a ** 2
    return b


if __name__ == '__main__':
    some(6, 8, 7, 6, 6)