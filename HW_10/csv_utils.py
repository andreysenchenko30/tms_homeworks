import csv


def csv_read(some_file):
    with open(some_file, 'r') as file_1:
        file_to_read = csv.reader(file_1)
        list_of_rows = []
        for row in file_to_read:
            list_of_rows.append(row)
        return list_of_rows


def csv_write(some_file):
    with open(some_file, 'w') as file_1:
        file_to_write = csv.writer(file_1)
        fields = ['firstname', 'lastname', 'group']
        rows = [
            ['Alex', 'Varkalov', 'Z-21'],
            ['Max', 'Ivanov', 'Z-21'], ]
        file_to_write.writerow(fields)
        file_to_write.writerows(rows)


def add_row(some_file):
    with open(some_file, 'a') as file_1:
        file_to_add = csv.writer(file_1)
        new_list = []
        while True:
            new_row = input('Enter the values, after finished press "0"')
            if new_row == '0':
                break
            else:
                new_list.append(new_row)
        file_to_add.writerow(new_list)


def add_row_in_some_place(some_file):
    index = int(input('Enter the position'))
    new_list = []
    while True:
        new_row = input('Enter the values, after finished press "0"')
        if new_row == '0':
            break
        else:
            new_list.append(new_row)
    with open(some_file, 'r') as file_1:
        file_to_read = csv.reader(file_1)
        list_of_old_rows = []
        iterator = 1
        for old_row in file_to_read:
            if iterator < index:
                list_of_old_rows.append(old_row)
                iterator += 1
            elif iterator == index:
                list_of_old_rows.append(new_list)
                iterator += 1
            else:
                list_of_old_rows.append(old_row)
                iterator += 1
    with open(some_file, 'w') as file_1:
        file_to_write = csv.writer(file_1)
        file_to_write.writerows(list_of_old_rows)


def delete_last(some_file):
    with open(some_file, 'r') as file_1:
        file_to_read = csv.reader(file_1)
        list_of_old_rows = []
        for old_row in file_to_read:
            list_of_old_rows.append(old_row)
    del list_of_old_rows[-1]
    with open(some_file, 'w') as file_1:
        file_to_write = csv.writer(file_1)
        file_to_write.writerows(list_of_old_rows)


def delete_some_row(some_file, position: int):
    with open(some_file, 'r') as file_1:
        file_to_read = csv.reader(file_1)
        list_of_old_rows = []
        for old_row in file_to_read:
            list_of_old_rows.append(old_row)
    del list_of_old_rows[position - 1]
    with open(some_file, 'w') as file_1:
        file_to_write = csv.writer(file_1)
        file_to_write.writerows(list_of_old_rows)
