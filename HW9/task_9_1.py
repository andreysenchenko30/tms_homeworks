list_of_strings = iter(['свобода', 'равенство', 'братство'])
new_list_of_strings = []
string_index = 1
for string in list_of_strings:
    new_list_of_strings.append(f'{string_index} - {string}')
    string_index += 1
print(new_list_of_strings)

