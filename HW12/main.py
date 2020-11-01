from classes import Point, Triangle, Circle, Square
point1 = Point(x=0, y=2)
point2 = Point(x=1, y=0)
point3 = Point(x=5, y=0)
triangle_1 = Triangle(point_1=point1, point_2=point2, point_3=point3)

point1 = Point(x=0, y=2)
point2 = Point(x=2, y=0)
square_1 = Square(point_1=point1, point_2=point2)

circle_1 = Circle(radius=5, center_point=5)

figures_list = [triangle_1, square_1, circle_1]
for figure in figures_list:
    print(f'Периметр {figure.__class__.__name__} равен {figure.get_perimeter()}')
    print(f'Площадь {figure.__class__.__name__} равна {figure.get_square()}')
