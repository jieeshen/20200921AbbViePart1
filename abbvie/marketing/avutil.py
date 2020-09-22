"""
Sample module for AbbVie class
"""
FRUITS = ['apple', 'banana', 'mango']

def main():
    print("Hi Mom!! Look at me!")
    spam()
    toast()
    toast()
    toast()

def spam():
    """Spiced pork fat etc in a can"""
    print("Hello from spam()")


def _ham():  # "private" function
    print("    Hello from _ham()")


def toast():
    """Tasty grilled bread"""
    print("Hello from toast()")
    _ham()

print("MY NAME IS", __name__)

#  if I am run directly, do this;
if __name__ == '__main__':
    main()

