from datetime import date


x = 5    #   x = int(5)

a = dict()
a['mango'] = 17

b = dict()
b['mango'] = 32

# today is an instance of the datetime.date class
wombat = date.today()  # str representation is YYYY-MM-DD
print(wombat)

print(wombat.ctime())
print(wombat.month)
print(wombat.day)
print(wombat.year)

james_bd = date(2014, 8, 1)  #  date james_bd = new date(2014, 8, 1);

print(james_bd)
print(james_bd.year)


class Animal:  # inherits from 'object'
    def move(self):
        print("I am moving")


class Dog(Animal):

    def bark(self):
        print("woof! woof!")


class Cat(Animal):
    def meow(self):
        print("meow meow meow")

d1 = Dog()
d2 = Dog()
d3 = Dog()

print(d1, id(d1))
print(d2, id(d2))
print(d3, id(d3))

for dog in d1, d2, d3:
    dog.bark()

d1.move()

c1 = Cat()
c1.meow()
c1.move()

x = 5
y = "hello"

print(x, y)
print(str(x), str(y))

print(c1)
print(str(c1))   # call c1.__str__()

