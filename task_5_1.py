pupils = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Andrey',
        'Group': 41,
        'physics': 9,
        'informatics': 9,
        'history': 9,
    },
    {
        'firstname': 'Anton',
        'Group': 43,
        'physics': 6,
        'informatics': 6,
        'history': 0,
    },
    {
        'firstname': 'Vlad',
        'Group': 42,
        'physics': 2,
        'informatics': 2,
        'history': 3,
    },
    {
        'firstname': 'Nastya',
        'Group': 42,
        'physics': 2,
        'informatics': 1,
        'history': 1,
    },
    {
        'firstname': 'Margo',
        'Group': 41,
        'physics': 10,
        'informatics': 10,
        'history': 10,
    },
    {
        'firstname': 'Alex',
        'Group': 42,
        'physics': 3,
        'informatics': 2,
        'history': 1,
    },
]
inf_sum = 0
for pupil in pupils:
    for key in pupil.keys():
        if key == 'informatics':
            inf_sum += pupil[key]
inf_av = inf_sum/len(pupils)
print(f'Средний балл по информатике: {inf_av}')

phys_sum = 0
for pupil in pupils:
    for key in pupil.keys():
        if key == 'physics':
            phys_sum += pupil[key]
phys_av = phys_sum/len(pupils)
print(f'Средний балл по физике: {phys_av}')

history_sum = 0
for pupil in pupils:
    for key in pupil.keys():
        if key == 'history':
            history_sum += pupil[key]
history_av = history_sum/len(pupils)
print(f'Средний балл по истории: {history_av}')

gpa = 0
sum_grades = 0
for pupil in pupils:
    for key in pupil.keys():
        sum_grades = pupil['history'] + pupil['physics'] + pupil['informatics']
        gpa = sum_grades/3
    if gpa > 4:
        print(f'Имя: {pupil["firstname"]}, Группа: {pupil["Group"]}, Информатика: {pupil["informatics"]}, Физика: {pupil["physics"]}, История: {pupil["history"]}, Средний балл: {gpa}')
