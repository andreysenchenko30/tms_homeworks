import csv_utils
import csv
text = csv_utils.csv_read('task.csv')


def price_sum():
    summa = 0
    for rows in text:
        for cells in rows:
            if rows.index(cells) == 1:
                try:
                    summa += int(cells)
                except ValueError:
                    pass
    print(f'Общая сумма: {summa}')


def the_most_expensive():
    biggest_price = 0
    most_expensive = ''
    for rows in text:
        try:
            if int(rows[1]) > biggest_price:
                biggest_price = int(rows[1])
                most_expensive = rows[0]
        except ValueError:
            pass
    print(f'Самый дорогой товар: {most_expensive}')


def the_cheapest():
    lowest_price = 100
    cheapest_item = ''
    for rows in text:
        try:
            if int(rows[1]) < lowest_price:
                lowest_price = int(rows[1])
                cheapest_item = rows[0]
        except ValueError:
            pass
    print(f'Самый дешевый товар: {cheapest_item}')


def reduce_quantity(some_file):
    new_rows = []
    for row in text:
        new_rows.append(row)
    for line in new_rows:
        try:
            number = int(line[2])
            number -= 1
            line[2] = number
        except ValueError:
            pass
    with open(some_file, 'w') as file_1:
        file_to_write = csv.writer(file_1)
        file_to_write.writerows(new_rows)


price_sum()
the_most_expensive()
the_cheapest()
reduce_quantity('task.csv')
