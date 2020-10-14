import csv_utils
text = csv_utils.csv_read('task.csv')


def price_sum():
    summ = 0
    for rows in text:
        for cells in rows:
            if rows.index(cells) == 1:
                try:
                    summ += int(cells)
                except:
                    pass
    print(f'Общая сумма: {summ}')


def the_most_expensive():
    biggest_price = 0
    most_expensive = ''
    for rows in text:
        try:
            if int(rows[1]) > biggest_price:
                biggest_price = int(rows[1])
                most_expensive = rows[0]
        except:
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
        except:
            pass
    print(f'Самый дешевый товар: {cheapest_item}')


price_sum()
the_most_expensive()
the_cheapest()
