class Car:
    def __init__(self, brand: str, model: str, release_year: int, speed=0):
        self.__brand = brand
        self.__model = model
        self.__release_year = release_year
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def reversal(self):
        self.__speed *= -1


car = Car(brand='Renault', model='Sandero', release_year=2015)

car.increase_speed()
car.increase_speed()
car.increase_speed()
car.reversal()
car.decrease_speed()
car.stop()
print(car.speed)
