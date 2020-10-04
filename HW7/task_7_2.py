def count_lower_and_upper(some_string: str):
    if not some_string.isalpha():
        return 'Wrong input. Please enter only letters'
    else:
        number_of_lower = 0
        number_of_upper = 0
        new_dict = {}
        for symbol in some_string:
            if symbol.islower():
                number_of_lower += 1
            else:
                number_of_upper += 1
        new_dict.update({'in_lower_case': number_of_lower})
        new_dict.update({'in_upper_case': number_of_upper})
        return new_dict


some_string = input('Enter the string\n')
print(count_lower_and_upper(some_string))
