class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure(object):
    pass


class Circle(Figure):
    def __init__(self, center_point, radius: int):
        self.center_point = center_point
        self.radius = radius

    def get_perimeter(self):
        perimeter = self.radius * 6.28
        return perimeter

    def get_square(self):
        square = self.radius ** 2 * 3.14
        return square


class Square(Figure):
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def get_side(self):
        side = abs(self.point_1.x - self.point_2.x)
        return side

    def get_perimeter(self):
        side = Square.get_side(self)
        perimeter = side * 4
        return perimeter

    def get_square(self):
        side = Square.get_side(self)
        square = side ** 2
        return square


class Triangle(Figure):
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def get_side_1(self):
        side_1 = ((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2) ** 0.5
        return side_1

    def get_side_2(self):
        side_2 = ((self.point_2.x - self.point_3.x) ** 2 + (self.point_2.y - self.point_3.y) ** 2) ** 0.5
        return side_2

    def get_side_3(self):
        side_3 = ((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2) ** 0.5
        return side_3

    def get_perimeter(self):
        side_1 = Triangle.get_side_1(self)
        side_2 = Triangle.get_side_2(self)
        side_3 = Triangle.get_side_3(self)
        perimeter = side_1 + side_2 + side_3
        return perimeter

    def get_square(self):
        side_1 = Triangle.get_side_1(self)
        side_2 = Triangle.get_side_2(self)
        side_3 = Triangle.get_side_3(self)
        half_perimeter = Triangle.get_perimeter(self) / 2
        square = (half_perimeter * (half_perimeter-side_1) * (half_perimeter-side_2) * (half_perimeter-side_3)) ** 0.5
        return square
