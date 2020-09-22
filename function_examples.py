"""
Demonstration of Python functions
"""
from typing import List  # Int Str Dict Tuple Set Any Union ...

# business logic
def get_message():
    """Get a message for the world"""
    return "Hello AbbVie world"

m = get_message()

print("m is", m)

# presentation logic; AKA user interface (UI) AKA user experience (UX)
def display_message():
    """Retrieve and display a message"""
    m = get_message()
    print(m)
    # return None

display_message()

x = display_message()
print("x is", x)

def spam():
    pass

spam()
print(spam())


def greet(whom: str) -> None:
    """Say hello to someone"""
    print("Hello,", whom)

greet("world")  # arguments are copied to parameters
greet("Uncle Billy")
greet("2020")
greet(1234)
greet(123.456)
greet(['this', 'is', 'wrong'])


x = """
char *doit(int x, float y) {
    /* blah blah blah */
    return "OK";
}

doit(5.6, 8);

"""

list_of_ints = List[int]

def double(some_ints: list_of_ints) -> list_of_ints:
    return [x * 2 for x in some_ints]

double([1, 2, 3])
double(['a', 'b', 'c'])

def ham(a, b, c, *others):  # *param allows optional parameter
    print("ham():", a, b, c, others)

ham(1, 2, 3)
ham('a', 'b', 'c')
ham('a', 'b', 'c', 'd', 'e', 'f')

#                iterable -- any object that can be looped over
def eggs(a, b, c, others):
    pass

def howdy(whom="world"):
    print("Howdy,", whom)

howdy('bro')
howdy('partner')
howdy()

def process(*, filename, max_size=5000):
    print(f"filename: {filename} max_size: {max_size}")

process(filename='wombat.txt', max_size=10000)
process(max_size=42000, filename='koala.dat')
process(filename='gorilla.txt')

def config(**values):
    print("values:", values)

config(color="blue", city="Chicago", element="iron")


# NAMING CONVENTIONS:

# global variables UPPER_CASE_WORDS_WITH_UNDERSCORES (but avoid globals if possible)
# everything except for classes:  lower_case_words_with_underscores
# classes:  MixedCase

#  customer_id_long
#  cid_lg

def read_csv_file():
    pass

class CSVFile:
    """This is a class to ..."""
    pass


