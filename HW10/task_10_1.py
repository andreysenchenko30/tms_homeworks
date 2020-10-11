from functools import reduce
divide_by_three = filter(lambda number: number % 3 == 0, [1, 2, 3, 4, 5, 6, 9, 12])
result = reduce(lambda filtered_number, next_filtered: filtered_number * next_filtered, list(divide_by_three), 1)
print(result)
