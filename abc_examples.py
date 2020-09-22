from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def move(self):
        pass

    def die(self):
        print("goodbye")

class Dog(Animal):
    def move(self):
        print("trotting along swiftly")

    def bark(self):
        print("woof woof!")


d1 = Dog()
d1.move()
d1.bark()

if issubclass(type(d1), Animal):
    d1.move()
    d1.die()




