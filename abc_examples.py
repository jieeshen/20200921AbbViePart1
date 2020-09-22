from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def move(self):
        pass

    def die(self):
        print("goodbye")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):  # getter property
        return self._name

    @name.setter
    def name(self, value):  # setter property
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name can only be a string")

    def move(self, how_fast="normally"):
        print(f"trotting along {how_fast}")

    def bark(self, bark_style="woof", how_many=1):
        print((bark_style + ' ') * how_many + "!")

    @staticmethod
    def fetch():
        print("Fetching")


d1 = Dog('Andy')
d1.move("slowly")
d1.bark()
print(d1.name)  # 0-argument method
d1.name = "Nellie"
print(d1.name)

if issubclass(type(d1), Animal):
    d1.move("swiftly")
    d1.die()

d1.move()
Dog.fetch()





d1.bark("yip", 5)


d1.fetch()
