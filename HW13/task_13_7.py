from random import randint


class Matrix(object):
    def __init__(self, data=None, n=5, m=5):
        if data is None:
            data = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.n = n
        self.m = m
        self.data = data

    def __str__(self):
        full_matrix = ''
        for line in self.data:
            row = ''
            for element in line:
                row += f'{element} '
            full_matrix += f'{row}\n'
        return full_matrix

    def randomize(self):
        self.n = randint(1, 10)
        self.m = randint(1, 10)
        self.data = []
        for line in range(self.n):
            line = []
            for element in range(self.m):
                element = randint(0, 100)
                line.append(element)
            self.data.append(line)


matrix1 = Matrix()
matrix1.randomize()
print(matrix1.__str__())


def get_max(matrix: Matrix()):
    max_element = 0
    for line in matrix.data:
        for element in line:
            if element > max_element:
                max_element = element
    return max_element


def get_min(matrix: Matrix()):
    min_element = 101
    for line in matrix.data:
        for element in line:
            if element < min_element:
                min_element = element
    return min_element


def element_sum(matrix: Matrix()):
    sum_of_elements = 0
    for line in matrix.data:
        for element in line:
            sum_of_elements += element
    return sum_of_elements


if __name__ == '__main__':
    print(f'Максимальный элемент: {get_max(matrix1)}')
    print(f'Минимальный элемент: {get_min(matrix1)}')
    print(f'Сумма элементов: {element_sum(matrix1)}')
