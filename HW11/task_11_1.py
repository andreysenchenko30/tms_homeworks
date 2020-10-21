class Dog:
    def __init__(self, master, name, age):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        return 'Jump!'

    def run(self):
        return 'Run!'

    def sleep(self):
        return 'Sleep!'

    def bark(self):
        return 'Woof!'

    def birthday(self):
        self.age += 1
        return self.age


dog = Dog(name='Richi', age=9, master='Zwergschnauzer')

print(dog.bark(), dog.jump(), dog.run(), dog.sleep(), dog.birthday())


class Cat:
    def __init__(self, master, name, age):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        return 'Jump!'

    def run(self):
        return 'Run!'

    def sleep(self):
        return 'Sleep!'

    def meow(self):
        return 'Meow!'

    def birthday(self):
        self.age += 1
        return self.age


cat = Cat(name='Rimus', age=3, master='British')

print(cat.meow(), cat.jump(), cat.run(), cat.sleep(), cat.birthday())


class Parrot:
    def __init__(self, master, name, age):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        return 'Jump!'

    def run(self):
        return 'Run!'

    def sleep(self):
        return 'Sleep!'

    def fly(self):
        return 'Fly!'

    def birthday(self):
        self.age += 1
        return self.age


parrot = Parrot(name='George', age=7, master='Ara')

print(parrot.fly(), parrot.jump(), parrot.run(), parrot.sleep(), parrot.birthday())
