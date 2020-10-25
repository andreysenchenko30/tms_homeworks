class Cow:
    def __init__(self, color='black&white', name='Polly', age=5):
        self.__name = name
        self.__age = age
        self.__color = color

    def run(self):
        return 'Run!'

    def moo(self):
        return 'Moo!'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Sheep:
    def __init__(self, color='white', name='Dolly', age=7):
        self.__name = name
        self.__age = age
        self.__color = color

    def run(self):
        return 'Run!'

    def bleat(self):
        return 'Baa!'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Rooster:
    def __init__(self, color='black', name='John', age=3):
        self.__name = name
        self.__age = age
        self.__color = color

    def run(self):
        return 'Run!'

    def crow(self):
        return 'cock-a-doodle-doo!'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Lion:
    def __init__(self, color='gold', name='Simba', age=7):
        self.__name = name
        self.__age = age
        self.__color = color

    def run(self):
        return 'Run!'

    def growl(self):
        return 'Arr!'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Wolf:
    def __init__(self, color='grey', name='Woofy', age=10):
        self.__name = name
        self.__age = age
        self.__color = color

    def run(self):
        return 'Run!'

    def bite(self):
        return 'I bit you!'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
