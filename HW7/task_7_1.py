def values_from_list(first_list: list):
    new_list = []
    for element in first_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


first_list = [3, 4, 3, 5, 6, 6, 7, 8]
print(f'Unique values from the first list: {values_from_list(first_list)}')
