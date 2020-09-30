def inches_in_cm():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int * 2.54
        return new_value
    else:
        return 'Wrong input'


def cm_in_inches():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int / 2.54
        return new_value
    else:
        return 'Wrong input'


def miles_in_km():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int * 1.609
        return new_value
    else:
        return 'Wrong input'


def km_in_miles():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int / 1.609
        return new_value
    else:
        return 'Wrong input'


def pounds_in_kg():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int / 2.205
        return new_value
    else:
        return 'Wrong input'


def kg_in_pounds():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int * 2.205
        return new_value
    else:
        return 'Wrong input'


def ounces_in_grams():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int * 28.35
        return new_value
    else:
        return 'Wrong input'


def grams_in_ounces():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int / 28.35
        return new_value
    else:
        return 'Wrong input'


def gallons_in_liters():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int * 3.785
        return new_value
    else:
        return 'Wrong input'


def liters_in_gallons():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int / 3.785
        return new_value
    else:
        return 'Wrong input'


def pints_in_liters():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int * 0.568
        return new_value
    else:
        return 'Wrong input'


def liters_in_pints():
    value = input('Введите начальное значение (целое число)\n')
    if value.isdigit():
        value_int = int(value)
        new_value = value_int / 0.568
        return new_value
    else:
        return 'Wrong input'


print('Доступные опции конвертера: \n\n1. Дюймы в сантиметры \n2. Сантиметры в дюймы \n'
      '3. Мили в километры \n4. Километры в мили \n5. Фунты в килограммы \n6. Килограммы в фунты \n'
      '7. Унции в граммы\n8. Граммы в унции \n9. Галлоны в литры \n'
      '10. Литры в галлоны \n11. Пинты в литры \n12. Литры в пинты\n')
while True:
    variant_of_conversion = input('Какой вариант вам нужен? Введите цифру от 1 до 12\n'
                                  'Для выхода из программы нажмите "0"\n')
    if variant_of_conversion.isdigit():
        if int(variant_of_conversion) == 1:
            print(f'Конвертированное значение: {inches_in_cm()}')
        elif int(variant_of_conversion) == 2:
            print(f'Конвертированное значение: {cm_in_inches()}')
        elif int(variant_of_conversion) == 3:
            print(f'Конвертированное значение: {miles_in_km()}')
        elif int(variant_of_conversion) == 4:
            print(f'Конвертированное значение: {km_in_miles()}')
        elif int(variant_of_conversion) == 5:
            print(f'Конвертированное значение: {pounds_in_kg()}')
        elif int(variant_of_conversion) == 6:
            print(f'Конвертированное значение: {kg_in_pounds()}')
        elif int(variant_of_conversion) == 7:
            print(f'Конвертированное значение: {ounces_in_grams()}')
        elif int(variant_of_conversion) == 8:
            print(f'Конвертированное значение: {grams_in_ounces()}')
        elif int(variant_of_conversion) == 9:
            print(f'Конвертированное значение: {gallons_in_liters()}')
        elif int(variant_of_conversion) == 10:
            print(f'Конвертированное значение: {liters_in_gallons()}')
        elif int(variant_of_conversion) == 11:
            print(f'Конвертированное значение: {pints_in_liters()}')
        elif int(variant_of_conversion) == 12:
            print(f'Конвертированное значение: {liters_in_pints()}')
        elif int(variant_of_conversion) == 0:
            break
        else:
            print('Такого варианта нет. Попробуйте еще раз')
    else:
        print('Ошибка ввода. Попробуйте еще раз')
